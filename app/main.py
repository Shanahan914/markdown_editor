from fastapi import FastAPI
from .database import create_db_and_tables
from .routes import router as all_routes
import uvicorn


app = FastAPI(title='Markdown Editor',
              description='check the grammar of your notes and render in html')

# register the routes in the app
app.include_router(all_routes)

# create db and tables
@app.on_event("startup")
def on_start():
    create_db_and_tables()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)