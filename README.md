## Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (or any other virtual environment tool)

## Installation

1. Create a new virtual environment:

python -m venv env
scheme

2. Activate the virtual environment:

- On Windows:
  ```
  env\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source env/bin/activate
  ```

3. Install the project dependencies

4. Apply the database migrations:

python manage.py migrate

5. Create a superuser (admin account) for the Django admin interface:

python manage.py createsuperuser

## Running the Development Server

1. Start the Django development server:

python manage.py runserver

2. Open your web browser and go to `http://localhost:8000/stripe/dashboard/` to see the project.

## Running Tests

To run the tests for your Django project:

python manage.py test

This will run all the tests defined in your project.
