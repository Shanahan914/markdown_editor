# Markdown Notes API

A RESTful API service that allows users to manage Markdown notes with grammar checking capabilities.

Completed as a solution to the roadmapsh markdown project - https://roadmap.sh/projects/markdown-note-taking-app

## Features

- Grammar validation for notes
- Save and store Markdown notes
- List all saved notes
- Convert and render Markdown notes to HTML

## API Endpoints

### Grammar Check
```
GET /notes/{id}/check-grammar
```
Validates the grammar of the provided note text.

### Save Note
```
POST /notes
```
Saves a new Markdown note to the system.

### List Notes
```
GET /notes
```
Retrieves a list of all saved Markdown notes.

### Render Note
```
GET /notes/{id}
```
Returns the HTML-rendered version of a specific Markdown note.

## Getting Started

### Prerequisites
see requirement.txt

### Installation
```bash
# Clone the repository
git clone https://github.com/Shanahan914/markdown_editor

# Navigate to project directory
cd markdown_editor

# Install dependencies
pip install -r requirements.txt
```

### Configuration
Create your .env file with your postgres details (owner and pg_password)

## Usage

1. Start the server:
```bash
python3 -m app.main
```

2. The API will be available at `http://localhost:8000`

## API Documentation

### Grammar Check Endpoint
- **URL**: `/notes/{id}/check-grammar`
- **Method**: `GET`
- **Request Body**: 
```json
{
    "text": "Your markdown text here"
}
```

### Save Note Endpoint
- **URL**: `/notes`
- **Method**: `POST`
- **Request Body**: 
```json
{
    "content": "# Your Markdown Content"
}
```

### List Notes Endpoint
- **URL**: `/notes`
- **Method**: `GET`
- **Response**: Returns an array of saved notes

### Render Note Endpoint
- **URL**: `/notes/{id}`
- **Method**: `GET`
- **Response**: Returns HTML content

