# 📘 Assignment: Task Manager with SQLite

## 🎯 Objective

Build a command-line task manager that stores tasks in a SQLite database. Practice creating a table, running parameterized SQL queries, and keeping data between program runs with Python's standard library.

## 📝 Tasks

### 🛠️ Create and Initialize the Database

#### Description
Complete the database setup function in the starter code. Run the program and confirm it creates a local SQLite database and a `tasks` table with an ID, task title, and completion status.

#### Requirements
Completed program should:

- Use Python's built-in `sqlite3` module without installing extra packages
- Create the `tasks` table if it does not already exist
- Give each task an integer ID and a completion status that defaults to incomplete


### 🛠️ Add and List Tasks

#### Description
Implement the functions that save a new task and retrieve all saved tasks. Use SQL placeholders and pass user-provided values separately to each query.

#### Requirements
Completed program should:

- Save a task title to the database and display the new task's ID
- List each task's ID, title, and completion status
- Show a helpful message when there are no tasks
- Preserve tasks after the program exits and starts again


### 🛠️ Mark Tasks as Complete

#### Description
Implement the function that marks a task complete using its ID. Try it with both an existing ID and an ID that is not in the database.

#### Requirements
Completed program should:

- Update only the task with the requested ID
- Report whether a task was updated or the ID was not found
- Keep the updated status when the program is restarted