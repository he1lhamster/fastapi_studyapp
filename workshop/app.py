
from fastapi import FastAPI

from .api import router

tags_metadata = [
    {
        'name': 'auth',
        'description': 'Authorization and Registration',
    },
    {
        'name': 'operations',
        'description': 'CRUD for operations',
    },
    {
        'name': 'reports',
        'description': 'Import and Export from DB',
    },
]

app = FastAPI(
    title='Workshop',
    description='Service for Study Fastapi',
    version='1.0.0',
    openapi_tags=tags_metadata,
)
app.include_router(router)

