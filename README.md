
# Study Planner API

## Project Description

Study Planner API is a REST API developed using FastAPI and Python. It helps users manage study tasks by creating, viewing, updating, and deleting tasks.

Each task contains a title, subject, priority, completion status, and estimated study time.

## Features

- View all study tasks.
- View a specific task using its ID.
- Create a new study task.
- Update an existing study task.
- Delete a study task.
- Filter tasks using supported query parameters.
- Test API endpoints using Swagger UI.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Swagger UI

## Project Structure

```text
study_planner_api/
├── main.py
├── README.md
└── venv/
```

## Installation and Setup

### 1. Clone the Repository

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

```bash
uvicorn main:app --reload
```

The API will run at:

http://127.0.0.1:8000

## API Documentation

FastAPI automatically generates interactive API documentation.

Open the following URL in your browser:

http://127.0.0.1:8000/docs

Click **Try it out** to test an endpoint, provide the required input, and click **Execute** to view the response.

## API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Display the welcome message |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{task_id}` | Retrieve a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update an existing task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Example Task Request

The following JSON represents a study task:

```json
{
  "title": "Practice FastAPI",
  "subject": "Backend",
  "priority": "high",
  "completed": false,
  "estimated_minutes": 75
}
```

## HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 | Request completed successfully |
| 201 | Resource created successfully |
| 204 | Resource deleted successfully; no response body |
| 404 | Requested task was not found |

## Data Storage

Task data is stored in memory in the current implementation. Therefore, tasks may be lost when the application restarts.

## Author

Asmita Pandeya
