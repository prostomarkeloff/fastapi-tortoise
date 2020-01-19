# FastAPI Tortoise

Here I was tried to describe how to use it and that ideas I followed when was creating it.

## Main ideas

    * All typed.
    I very like modern Python. Python with type-hints. It let to you write a code that will be understood by everybody.
    * All tested.
    I'm a big fan of TDD ideas. I have tried to test all components in this project.
    * Respects to OpenAPI ideas.
    OpenAPI schema is great thing, really. When I was creating it I was hoping that you will use the OpenAPI capatibilites which FastAPI provides to you fully.
    * Easy to deploy.
    No comments.

## The project structure

`app/main.py` is the file which will import `uvicorn`, in this file you should call initializer functions.

`app/initializer.py` is the file which will be called by `app/main.py` for application initializing. Out of the box it's initializing the database and API routers.

`app/api/...` here you should define the routes. In `app/api/__init__.py` you should import routers and init `TypedAPIRouter`s for much pretty tags, dependencies and etc initialization.

`app/utils/...` here you may create a needed for your projects utilites.

`app/models/...` Tortoise and Pydantic models of database entities.

`app/exceptions/...` exceptions for your API, just like `fastapi.HTTPException` but for your needs.

`app/config/...` config for your project. You always can change it but please, try use the `pydantic.BaseSettings` - it really good thing.

TBD