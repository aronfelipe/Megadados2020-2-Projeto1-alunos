# pylint: disable=missing-module-docstring,missing-class-docstring
from typing import Optional

from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module

import uuid

# pylint: disable=too-few-public-methods
class Task(BaseModel):
    description: Optional[str] = Field(
        'no description',
        title='Task description',
        max_length=1024,
    )
    completed: Optional[bool] = Field(
        False,
        title='Shows whether the task was completed',
    )

    user_uuid: uuid.UUID = Field(
        title='User identification'
    )

    class Config:
        schema_extra = {
            'example': {
                'description': 'Buy baby diapers',
                'completed': False,
                'user_uuid' : "4061b606-998f-46e6-841a-ace5ae015a14",
            }
        }

class User(BaseModel):
    name: Optional[str] = Field(
        'name',
        title='Name',
        max_length=1024,
    )

    class Config:
        schema_extra = {
            'example': {
                'Name': 'Luquinha',
            }
        }
