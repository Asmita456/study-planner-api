
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
- Filter tasks by subject, completion status, and priority.
- Search tasks by title.
- Sort tasks by title or estimated study time.
- Paginate task results using skip and limit.
- View a summary of tasks, including completed tasks, pending tasks, and estimated study time.
- Handle errors when a task does not exist.
- Automatically generated API documentation using Swagger UI.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Swagger UI

## Project Structure

```text
study_planner_api/
├── app/
│   ├── main.py
│   ├── routers/
│   │   └── tasks.py
│   └── schemas/
│       └── task.py
├── README.md
└── venv/
```

*Note: The virtual environment folder is local and should not be uploaded to GitHub.*

## Installation and Setup

### 1. Clone the Repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd study_planner_api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install fastapi uvicorn
```

### 5. Run the Application

Run the following command from the project root directory:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

## API Documentation

FastAPI automatically generates interactive API documentation.

Open Swagger UI in your browser:

http://127.0.0.1:8000/docs

To test an endpoint:

1. Expand the endpoint.
2. Click **Try it out**.
3. Enter the required parameters or JSON request body.
4. Click **Execute**.
5. Review the response and HTTP status code.

## API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Display the welcome message |
| GET | `/tasks` | Retrieve and filter tasks |
| GET | `/tasks/summary` | View the task summary |
| GET | `/tasks/{task_id}` | Retrieve a specific task |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update an existing task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Task Fields

Each task contains the following fields:

- `id`: Unique identifier of the task.
- `title`: Name of the study task.
- `subject`: Subject or study area.
- `priority`: Priority level of the task.
- `completed`: Indicates whether the task is completed.
- `estimated_minutes`: Estimated time required to complete the task, in minutes.

## Example Request Body

Use the following JSON when creating a task:

```json
{
  "title": "Practice FastAPI",
  "subject": "Backend",
  "priority": "high",
  "completed": false,
  "estimated_minutes": 75
}
```

The API generates the task ID automatically.

## Filtering, Searching, Sorting, and Pagination

The `GET /tasks` endpoint supports the following query parameters:

| Parameter | Description |
|---|---|
| `subject` | Filter tasks by subject |
| `completed` | Filter by completion status |
| `search` | Search within task titles |
| `priority` | Filter by priority |
| `skip` | Number of tasks to skip; default is 0 |
| `limit` | Maximum number of tasks returned; default is 10, maximum is 20 |
| `sort_by` | Sort by `title` or `estimated_minutes` |
| `order` | Sort in ascending (`asc`) or descending (`desc`) order |

### Example Query

```text
/tasks?subject=Python&completed=false
```

This returns incomplete tasks whose subject is Python, subject to the default sorting and pagination settings.

Another example:

```text
/tasks?sort_by=estimated_minutes&order=desc&skip=0&limit=5
```

This returns up to five tasks sorted by estimated study time from highest to lowest.

## Task Summary

The `GET /tasks/summary` endpoint provides an overview of study tasks, including:

- Total number of tasks.
- Number of completed tasks.
- Number of pending tasks.
- Total estimated study time for all tasks.
- Remaining estimated study time for incomplete tasks.

## HTTP Status Codes

| Status Code | Meaning |
|---|---|
| `200 OK` | Request completed successfully |
| `201 Created` | A new task was created successfully |
| `204 No Content` | A task was deleted successfully |
| `400 Bad Request` | Invalid sorting parameter |
| `404 Not Found` | The requested task does not exist |

### Example Error Response

If a task with the requested ID does not exist, the API returns:

```json
{
  "detail": "Task not found"
}
```

## Data Storage

The current implementation stores tasks in an in-memory Python list. No database is used.

As a result, task changes are temporary and may be lost when the application restarts.

## Author

**Asmita Pandeya**
