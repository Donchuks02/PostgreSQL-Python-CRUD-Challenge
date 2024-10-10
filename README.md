# PostgreSQL + Python CRUD Challenge

This project demonstrates how to perform basic CRUD (Create, Read, Update, Delete) operations using PostgreSQL with Python. The project is organized in a modular fashion, with each CRUD operation defined in its own file, and the database configuration handled via a `database.ini` file for ease of use and maintainability.This project now also includes functionality for managing departments and associating users with multiple departments.

# ###########################################################################################

## Updates
Now departments table has been added and user can belong to one or many departments.
### Recent Additions
- **Departments Table**: A new `departments` table has been added to store department names. Each department name is unique.
- **User-Departments Relationship**: A new `user_departments` table has been introduced to establish a many-to-many relationship between users and departments. This table references the `users` table by user ID and the `departments` table by department name.

### Updated Scripts
- **`create_table.py`**: Modified to include the creation of `departments` and `user_departments` tables, along with necessary foreign key constraints.
- **`insert_user.py`**: Updated to include functions for inserting multiple departments and user-department relationships.

### Example Usage
To insert departments and associate them with users, use the following functions in `insert_user.py`:
- `insert_many_departments`: Inserts multiple departments into the `departments` table.
- `insert_user_departments`: Associates users with departments in the `user_departments` table.

# #####################################################################################################

## Task: Write a Python script using psycopg2 or SQLAlchemy to connect to a PostgreSQL database. Perform basic CRUD (Create, Read, Update, Delete) operations on a simple users table with columns id, name, email, and date_joined.
Goal: Ensure you understand how to create connections, execute queries, and handle transactions.

## Table of Contents
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [CRUD Operations Overview](#crud-operations-overview)
- [Viewing Recent Data](#viewing-recent-data)
- [Error Handling](#error-handling)
- [Conclusion](#conclusion)

## Project Structure

```
project_directory/
├── create_table.py        # Script for creating the 'users' table
├── database.ini           # Configuration file for database credentials
├── DB_config_file.py      # database credentials setup
├── DB_connection_file.py  # database connection setup
├── delete_user.py         # Script for deleting user
├── insert_user.py         # Script for inserting users into the database
├── view_recent_data.py    # Entry point of the project
├── README.md              # README file
├── update_user.py         # Script for updating user information
├── view_recent_data.py    # Script for viewing the most recent data from the 'users' table
```

## Requirements
To run this project, you will need:
- Python 3.7+
- PostgreSQL installed and running locally or remotely
- Python packages:
  - `psycopg2`
  - `configparser`

You can install the required Python packages using:
```bash
pip install psycopg2
```

## Setup and Installation

### 1. Clone the Repository
```bash
git clone <repository_url>
cd project_directory
```

### 2. Install PostgreSQL
Ensure that you have PostgreSQL installed and running. You can download PostgreSQL from [here](https://www.postgresql.org/download/).

### 3. Create a PostgreSQL Database
Log in to your PostgreSQL instance and create a database:
```sql
CREATE DATABASE crud;
```

## Configuration

This project uses a `database.ini` file to store the PostgreSQL connection details. Here's how you should configure it:

### database.ini
```ini
[postgresql]
host = localhost
database = crud
user = postgres
password = your_password
```

- `host`: Your PostgreSQL server (usually `localhost` if local)
- `database`: The name of the database (`crud`)
- `user`: Your PostgreSQL username
- `password`: Your PostgreSQL password

## Running the Project

Once your environment is set up, you can start executing the CRUD operations:

### 1. Create the Users Table
```bash
python create_table.py
```
This will drop the `users` table if it exists and create a new one.

### 2. Insert New Users
```bash
python insert_user.py
```
This will insert a list of predefined users into the database.

### 3. Update a User's Information
```bash
python update_user.py
```
This will update the information for a specific user in the `users` table.

### 4. Delete a User
```bash
python delete_user.py
```
This will delete a user based on the user ID.

### 5. Fetch and View All Users
```bash
python view_recent_data.py
```
This script fetches and displays all users stored in the `users` table.

## CRUD Operations Overview

Each CRUD operation (Create, Read, Update, Delete) is handled by its respective Python file:

- **Create**: Defined in `create_table.py`, which sets up the table in the PostgreSQL database.
- **Insert**: Defined in `insert_user.py`, which inserts predefined users into the database.
- **Update**: Defined in `update_user.py`, which updates a user’s name based on their ID.
- **Delete**: Defined in `delete_user.py`, which removes a user based on their name.
- **Fetch**: Defined in `view_recent_data.py`, which retrieves all users from the database.

## Viewing Recent Data

To view the most recent data from the database (e.g., users ordered by their join date), use the `view_recent_data.py` script. This script orders the results by the `id` field.

Run the script:
```bash
python view_recent_data.py
```

## Error Handling

The project includes basic error handling for database operations. If an error occurs during any operation (e.g., a failed connection to the database), an appropriate message is printed to the console.

Example:
```bash
Unable to connect to the database: <error_message>
```

## Conclusion

This project demonstrates how to perform CRUD operations on a PostgreSQL database using Python, with a clean separation of concerns. Each operation is modularized into its own file, and the project uses `configparser` to manage database connection details securely and efficiently.