# Frappe Application Setup

## Prerequisites

- Python 3.7+
- Node.js 14+
- Redis
- MariaDB
- Yarn

## Installation Steps

1. Install the Frappe Framework:

   ```bash
   bench init frappe-bench
   cd frappe-bench
   bench new-site taskmanager.local
   bench get-app frappe
   bench --site taskmanager.local install-app frappe
   bench start

## API Documentation

### Create Task

- *Endpoint*: /api/method/task_manager.api.task.create_task
- *Method*: POST
- *Parameters*: title, description, status (optional)
- *Response*: Task name

### Get Task

- *Endpoint*: /api/method/task_manager.api.task.get_task
- *Method*: GET
- *Parameters*: task_name
- *Response*: Task details

### Update Task

- *Endpoint*: /api/method/task_manager.api.task.update_task
- *Method*: PUT
- *Parameters*: task_name, title (optional), description (optional), status (optional)
- *Response*: Task name

### Delete Task

- *Endpoint*: /api/method/task_manager.api.task.delete_task
- *Method*: DELETE
- *Parameters*: task_name
- *Response*: Success message

## Database Schema

### Project

- project_name: Name of the project.
- tasks: List of tasks associated with the project.

### Task

- title: Title of the task.
- description: Description of the task.
- status: Current status of the task.

## Performance Optimization

- *Caching*: Frequently accessed task data is cached using Redis.
- *Pagination*: Large datasets are paginated to improve response times.

## Debugging Process

### Issue

- The sample application was throwing a 500 error when accessing the /api/method/sample_app.api.get_data endpoint.

### Resolution

- The issue was caused by a missing field in the DocType. After adding the required field, the API started working as expected.

API Documentation
Create Task
Endpoint: /api/method/task_manager.api.task.create_task

Method: POST
Parameters:
title (string): Title of the task (required).
description (string): Description of the task (required).
status (string, optional): Status of the task (default: "Open").
Response: Task name (string).
Get Task
Endpoint: /api/method/task_manager.api.task.get_task

Method: GET
Parameters:
task_name (string): Name of the task to fetch (required).
Response: Task details (JSON object).
Update Task
Endpoint: /api/method/task_manager.api.task.update_task

Method: PUT
Parameters:
task_name (string): Name of the task to update (required).
title (string, optional): New title for the task.
description (string, optional): New description for the task.
status (string, optional): New status for the task.
Response: Task name (string).
Delete Task
Endpoint: /api/method/task_manager.api.task.delete_task

Method: DELETE
Parameters:
task_name (string): Name of the task to delete (required).
Response: Success message (string).
Testing APIs with Postman
Step 1: Set Up Postman
Open Postman.
Create a new collection (e.g., Task Manager APIs).
Add the API endpoints to the collection.
Step 2: Test the APIs
Create Task
Method: POST
URL: <http://taskmanager.local:8000/api/method/task_manager.api.task.create_task>
Headers:
Content-Type: application/json
Authorization: Bearer <your_api_key> (if authentication is enabled).
Body (JSON):
json
Copy
Edit
{
  "title": "Complete Project Report",
  "description": "Finish the project report by Friday.",
  "status": "Open"
}
Response:
json
Copy
Edit
"TASK-0001"
Get Task
Method: GET
URL: <http://taskmanager.local:8000/api/method/task_manager.api.task.get_task?task_name=TASK-0001>
Headers:
Authorization: Bearer <your_api_key> (if authentication is enabled).
Response:
json
Copy
Edit
{
  "name": "TASK-0001",
  "title": "Complete Project Report",
  "description": "Finish the project report by Friday.",
  "status": "Open"
}
Update Task
Method: PUT
URL: <http://taskmanager.local:8000/api/method/task_manager.api.task.update_task>
Headers:
Content-Type: application/json
Authorization: Bearer <your_api_key> (if authentication is enabled).
Body (JSON):
json
Copy
Edit
{
  "task_name": "TASK-0001",
  "status": "In Progress"
}
Response:
json
Copy
Edit
"TASK-0001"
Delete Task
Method: DELETE
URL: <http://taskmanager.local:8000/api/method/task_manager.api.task.delete_task?task_name=TASK-0001>
Headers:
Authorization: Bearer <your_api_key> (if authentication is enabled).
Response:
json
Copy
Edit
"Task deleted successfully"
Caching Mechanism
Redis Caching: Frequently accessed task data is cached using Redis to improve performance.
Cache Key Format: task_<task_name>
Cache Invalidation: The cache is updated or cleared whenever a task is updated or deleted.
Database Schema
Task
Field Type Description
title string Title of the task
description string Description of the task
status string Current status of the task
Project
Field Type Description
project_name string Name of the project
tasks Table List of tasks associated with the project
Debugging
Check Frappe logs:
bash
Copy
Edit
bench --site taskmanager.local logs  
Use Postman's console: Debug requests and responses for troubleshooting.
License
This project is licensed under the MIT License. See the LICENSE file for details.

pgsql
Copy
Edit

This version ensures clarity, proper formatting, and an easy-to-read structure for your README file.
