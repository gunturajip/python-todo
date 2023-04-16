# Tudulis

Tudulis is an web app for CRUD-ing todo-list by authenticated and authorized users.

## Access Documentation

- Postman: -

To run the project locally, follow these steps:

1. Clone the repository
2. Initialize and activate a new virtual environment
   - For Windows:
     Type the following command in VS Code terminal:
     `
     python -m venv env
     `
     `
     env\Scripts\activate
     `
   - For Linux:
     Type the following command in VS Code terminal:
     `
     python3 -m venv env
     `
     `
     source bin/activate
     `
3. Install the required dependencies
     `
     pip install -r requirements.txt
     `
4. Set up the database and environment variables
5. Run the application using `flask run` or `flask run --debug`

## Support

If you find this project useful, please consider giving it a ⭐️ on [GitHub](https://github.com/gunturajip/python-todo). Your support is greatly appreciated!

## Endpoints

### User

| Method | Endpoint          | Description                       |
| ------ | ----------------- | --------------------------------- |
| POST   | `/register`       | Register a new user               |
| POST   | `/login`          | Login with existing user          |
| POST   | `/register`       | Logout of current user            |

### Todo

| Method | Endpoint                             | Description                              |
| ------ | ------------------------------------ | ---------------------------------------- |
| POST   | `/todo`                              | Create a new todo                        |
| GET    | `/todo`                              | Get a list of todo                       |
| GET    | `/todo/:todo_id`                     | Get a specific todo                      |
| PUT    | `/todo/:todo_id`                     | Update a specific todo                   |
| DELETE | `/todo/:todo_id`                     | Delete a specific todo                   |
| POST   | `/todo/:todo_id/completed`           | Mark a spefific todo as completed        |
| POST   | `/todo/:todo_id/uncompleted`         | Mark a specific todo as uncompleted      |
