# MyGram (Instagram Clone)

MyGram is an Instagram Clone for CRUD-ing photos, social media, and comments among users.
To-do:
- Need update for repository and service
- Optimize all code for shorter code and faster calculation
- Optimize swagger documentation for easier readibility

## Access Documentation

- Swagger: https://golang-mygram-production.up.railway.app/swagger/index.html

To run the project locally, follow these steps:

1. Clone the repository
2. Initialize and activate a new virtual environment
   - For Windows:
     Type the following command in VS Code terminal:
     `
     python -m venv env
     env\Scripts\activate
     `
   - For Windows:
     Type the following command in VS Code terminal:
     `
     python3 -m venv env
     source bin/activate
     `
3. Install the required dependencies
   - For Windows:
     `
     pip install flask flask_sqlalchemy flask_jwt_extended psycopg2 flask_migrate
     `
   - For Linux:
     `
     pip3 install flask flask_sqlalchemy flask_jwt_extended psycopg2 flask_migrate
     `
4. Set up the database and environment variables
   - For Windows:
     export .env vars in local dev using Git Bash:
     `
     export $(grep -v '^#' .env | xargs)
     `
5. Run the application using `python app.py`.

## Support

If you find this project useful, please consider giving it a ⭐️ on [GitHub](https://github.com/gunturajip/golang-mygram). Your support is greatly appreciated!

## Endpoints

| Method | Endpoint          | Description                       |
| ------ | ----------------- | --------------------------------- |
| POST   | `/users/register` | Register a new user               |

### Photos

| Method | Endpoint              | Description                  |
| ------ | --------------------- | ---------------------------- |
| POST   | `/photos/`            | Create a new photo           |
| GET    | `/photos/`            | Get a list of photos         |
| GET    | `/photos/:id`         | Get a specific photo         |
| PUT    | `/photos/:id`         | Update a specific photo      |
| DELETE | `/photos/:id`         | Delete a specific photo      |

### Comments

| Method | Endpoint              | Description                   |
| ------ | --------------------- | ----------------------------- |
| POST   | `/comments/`          | Create a new comment          |
| GET    | `/comments/`          | Get a list of comments        |
| GET    | `/comments/:id`       | Get a specific comment        |
| PUT    | `/comments/:id`       | Update a specific comment     |
| DELETE | `/comments/:id`       | Delete a specific comment     |

### Social Media

| Method | Endpoint                    | Description                   |
| ------ | --------------------------- | ----------------------------- |
| POST   | `/socialmedia/`             | Create a new media            |
| GET    | `/socialmedia/`             | Get a list of media           |
| GET    | `/socialmedia/:id`          | Get a specific media          |
| PUT    | `/socialmedia/:id`          | Update a specific media       |
| DELETE | `/socialmedia/:id`          | Delete a specific media       |