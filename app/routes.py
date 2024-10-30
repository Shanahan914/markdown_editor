from fastapi import UploadFile, HTTPException, APIRouter
from fastapi.responses import HTMLResponse
from typing import List 
from sqlmodel import select
from .schema import NoteMetaPublic, GrammarDataPublic
from .models import Note
from .database import SessionDep
import logging
import markdown
import language_tool_python


# initialize router

router = APIRouter()

# initialize logger 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# error handler and logger

def log_and_raise_error(message: str, status_code: int = 500):
    logger.error(message)
    raise HTTPException(status_code=status_code, detail=message)


# initialize language tool
tool = language_tool_python.LanguageTool('en-UK')


# upload file

@router.post("/")
async def upload_file(file: UploadFile, session : SessionDep) -> NoteMetaPublic:

    # Read the content from the uploaded file
    file_content = await file.read()
    try:
        markdown_text = file_content.decode("utf-8")  # Decode bytes to string
    except Exception as e:
        log_and_raise_error(f'failure to convert file to string. Ensure you have uploaded a .md file: {e}', 400)

    # save to db
    try:
        new_file = Note(filename = file.filename, content = markdown_text, version = 1)
        session.add(new_file)
        session.commit()
        session.refresh(new_file)
        return new_file
    except Exception as e:
        log_and_raise_error(f'error saving to database: {e}', 500)

    
# check grammar
@router.get('/notes/{id}/grammar')
def check_grammar(id: int, session: SessionDep) -> GrammarDataPublic:

    # get data from database
    note = session.get(Note, id)
    if note is None:
        log_and_raise_error(f'note does not exist or could not be found', 400)
    content = note.content
 

    # TODO change this into async
    matches = tool.check(content)
    corrected_file = tool.correct(content)
    grammar_issues = {}
    for id, match in enumerate(matches):
        grammar_issues[id] = {
            "offset": match.offset,
            "message": match.message,
            "replacements": match.replacements
        }
    grammar_data = {'errors': grammar_issues,
                    'corrected_version': corrected_file}
    return grammar_data


# list uploaded notes
@router.get('/notes')
def get_all_notes(session: SessionDep) -> List[NoteMetaPublic]:
    try:
        notes = session.exec(select(Note)).all()
        return notes
    except Exception as e:
        log_and_raise_error(f'error retrieving notes from database: {e}', 500)
        

# render a note
@router.get('/notes/{id}', response_class=HTMLResponse)
def render_single_note(id : int, session: SessionDep):
  
    # get info from database
 
    note = session.get(Note, id)
    if note is None:
        print('it is empty')
        raise HTTPException(status_code=400, detail="note does not exist or could not be found")
    try:
        content = note.content
        html = markdown.markdown(content)
    except Exception as e:
        log_and_raise_error(f"error converting markdown to html", 500)
    
    # render note
    return html