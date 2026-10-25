# Study Planner API

## Project Description

Study Planner API is a RESTful API developed using Python and FastAPI. It helps users organize and manage their study tasks through different API operations.

Each task contains a title, subject, priority, completion status, and estimated study time.

## Features

- View all study tasks.
- Retrieve a specific task using its ID.
- Create new study tasks.
- Update existing tasks.
- Delete tasks.
- Automatically generate unique task IDs.
- Validate task data using Pydantic.
- Filter tasks by subject, completion status, and priority.
- Search tasks by title.
- Sort tasks by title or estimated study time.
- Paginate task results using `skip` and `limit`.
- View a summary of completed tasks, pending tasks, and estimated study time.
- Handle errors when a task does not exist.
- Use automatically generated API documentation through Swagger UI.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Swagger UI

## Project Structure

study_planner_api/\
├── app/\
│   ├── init.py\
│   ├── routers/\
│   │   ├── init.py\
│   │   └── tasks.py\
│   └── schemas/\
│       ├── init.py\
│       └── task.py\
├── screenshots/\
├── main.py\
├── requirements.txt\
├── README.md\
└── .gitignore

Note: The `venv/` virtual environment and Python cache files are local development files and should not be uploaded to GitHub.

## Installation and Setup

### 1. Clone the Repository

git clone [https://github.com/Asmita456/study-planner-api.git](https://github.com/Asmita456/study-planner-api.git?utm_source=chatgpt.com)\
cd study-planner-api

### 2. Create a Virtual Environment

python -m venv venv

### 3. Activate the Virtual Environment

For Windows PowerShell:

.\venv\Scripts\Activate.ps1

### 4. Install Dependencies

python -m pip install -r requirements.txt

### 5. Run the Application

Run the following command from the project root directory, where `main.py` is located:

uvicorn main:app --reload

The API will be available at:

- API: [http://127.0.0.1:8000](http://127.0.0.1:8000?utm_source=chatgpt.com)
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs?utm_source=chatgpt.com)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc?utm_source=chatgpt.com)

## API Documentation

FastAPI automatically generates interactive API documentation using Swagger UI.

To test an endpoint:

1. Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs?utm_source=chatgpt.com) in your browser.
2. Expand the endpoint.
3. Click Try it out.
4. Enter the required parameters or JSON request body.
5. Click Execute.
6. Review the response body and HTTP status code.

## API Endpoints

| HTTP Method | Endpoint           | Description                 |
| ----------- | ------------------ | --------------------------- |
| GET         | `/`                | Display the welcome message |
| GET         | `/tasks`           | Retrieve and filter tasks   |
| GET         | `/tasks/{task_id}` | Retrieve a specific task    |
| POST        | `/tasks`           | Create a new task           |
| PUT         | `/tasks/{task_id}` | Update an existing task     |
| DELETE      | `/tasks/{task_id}` | Delete a task               |
| GET         | `/tasks/summary`   | View the task summary       |

## Task Fields and Validation

| Field               | Description                     | Validation                               |
| ------------------- | ------------------------------- | ---------------------------------------- |
| `id`                | Unique task identifier          | Generated automatically by the server    |
| `title`             | Name of the study task          | At least 3 characters                    |
| `subject`           | Subject or study area           | At least 2 characters                    |
| `priority`          | Priority level                  | `low`, `medium`, or `high`               |
| `completed`         | Completion status               | Defaults to `false` when creating a task |
| `estimated_minutes` | Estimated study time in minutes | Integer between 1 and 480                |

The PUT endpoint requires all editable fields: `title`, `subject`, `priority`, `completed`, and `estimated_minutes`. The task ID cannot be changed through the request body.

Invalid request data is rejected with HTTP `422 Unprocessable Entity`.

## Example Requests

### 1. Get Incomplete Python Tasks

GET /tasks?subject=python&completed=false

This returns tasks whose subject is Python and whose completion status is false. Subject matching is case-insensitive.

### 2. Create a New Study Task

Endpoint: `POST /tasks`

Request body:

{
  "title": "Practice FastAPI",
  "subject": "Backend",
  "priority": "high",
  "estimated_minutes": 75
}


Successful Response — 201 Created:
{
  "id": 6,
  "title": "Practice FastAPI",
  "subject": "Backend",
  "priority": "high",
  "completed": false,
  "estimated_minutes": 75
}

Note: The task ID in the response is an example. The actual ID depends on the tasks currently stored in memory.