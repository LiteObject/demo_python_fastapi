# Python FastAPI - Setup and Run Guide

This guide will walk you through the process of setting up and running a Python FastAPI application. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+.

## Prerequisites
Before getting started, ensure that you have the following installed on your system:

- Python 3.7 or above
- pip (Python package installer)

## Setup
1. Create a new directory for your FastAPI project.

        mkdir my_fastapi_project

2. Navigate into the project directory

        cd my_fastapi_project

2. Set up a virtual environment (optional, but recommended).

        python3 -m venv .venv

3. Activate the virtual env:

        .venv/scripts/activate

4. Install FastAPI and additional dependencies.

        pip install fastapi uvicorn

## Creating a FastAPI Application

1. Create a new Python file, for example `main.py`, in your project directory.

        touch main.py

2. Open `main.py` with your preferred text editor and import the necessary modules.

        from fastapi import FastAPI

3. Create an instance of the FastAPI class.

        app = FastAPI()

4. Define your API routes and their corresponding functions.

        @app.get("/")
        async def root():
            return {"message": "Hello World"}

## Running the FastAPI Application

1. Start the FastAPI application using the uvicorn server.

        uvicorn main:app --reload

The `main:app` argument specifies the Python file (main.py) and the instance of the FastAPI class (app).

2. Open your web browser and navigate to `http://localhost:8000` to see the root endpoint response.

3. To test the other endpoints, use the appropriate URL patterns. For example, `http://localhost:8000/items/42?q=test`.

## Conclusion
We have successfully set up and run a Python FastAPI application. This guide covered the basic steps to get us started with FastAPI and create simple API routes. FastAPI provides numerous features such as request validation, automatic API documentation generation, dependency injection, and more. Refer to the FastAPI documentation for further information on how to leverage these features and build powerful APIs.

## Links
- [Learn FastAPI](https://fastapi.tiangolo.com/learn/)