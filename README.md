# Description:

This is an app created specifically for the Finsure Back-end Engineering Challenge.

The main objective of the challenge is to create a RESTful API using Django. The API should be backed by a MariaDB database, conform to the JSON:API specification and should implement endpoints that provide the following functionality:

1. Create a new Lender
2. List all Lenders (five per page)
   1. List active lenders
3. Get a specific Lender
4. Update a specific Lender
5. Delete a specific Lender
6. Bulk upload Lenders in CSV format
7. Download Lenders in CSV format

# How to install:

1. Install Python 3.8
   1. Install `pipenv` using `pip install pipenv`
2. Install MariaDB
   1. Create a new database
3. Clone the repository
4. Navigate to project folder and run `pipenv install` or `pipenv install --dev` to include dev dependencies
5. Create a `.env` file in the project folder and add the folowing variables
```
# Debug mode
DEBUG_MODE=

# Secret key
SECRET_KEY=

# Database access
DATABASE_NAME=
DATABASE_HOST=
DATABASE_PORT=
DATABASE_USER=
DATABASE_PASS=
```
6. Run `pipenv run mg` to apply migrations

# How to run:

Run `pipenv run start`

# Extra info:

Additional shortcuts for Django manage commands can be found in the `Pipfile`