# Django Restframework API
This project implements a RESTful API using Django and Django REST framework. The API handles text search functionalities, allowing users to input multiple paragraphs of text and perform word searches within them.

## Features
- Input multiple paragraphs of text.
- Retrieve top paragraphs containing the searched word.

## Installation

Clone this repo by using the following command

`git clone https://github.com/subhani-syed/Text-Search-DRF.git .`

### Set Up a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.
1.  Create a virtual environment:
```
python -m venv venv
```
1. Activate the virtual environment:
```
source venv/bin/activate  # For Linux/macOS
.\venv\Scripts\activate   # For Windows
```
## Setup Running

### Use .env File

Create a `.env` file in the project root directory and define the environment variables needed for your application, such as database credentials, secret keys, etc. The below is an example
```
SECRET_KEY=your_secret_key
PG_USER=your_username
PG_PWD=your_pwd
PG_HOST=your_host
PG_DB=your_db
PG_PORT=your_db_port
POSTGRES_USER=postgre_user
POSTGRES_PASSWORD=postgre_pwd
POSTGRES_DB=postgre_db
```
## Setup and Running

### Docker Compose

This project uses Docker Compose for containerization. To run the application using Docker Compose:

1.  Make sure Docker is installed on your machine.
    
2.  Navigate to the project directory containing the `docker-compose.yml` file.
    
3.  Run the following command:
```
docker-compose up --build
```



This command will build and run the Docker containers for the Django app and PostgreSQL database.


## Documentation

### Postman Collection

Explore the API documentation using Postman Collection file named `Text Search API.postman_collection.json`. 
This interactive documentation provides details about available endpoints, request formats, and responses.

### Swagger UI
Alertnatievly, we can explore the API documentation using Swagger UI at [http://localhost:8000/api/swagger/](http://localhost:8000/api/swagger/)

## Technologies Used

- Django Rest Framework
- PostgreSQL
- drf-yasg (Swagger)
- Postman
- Docker
- Docker compose
