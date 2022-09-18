from pydantic import BaseModel, Extra, constr, validator, AnyHttpUrl, conlist
from typing import List


def snake_to_camel_case(value: str) -> str:
    if not isinstance(value, str):
        raise ValueError("Value must be a string.")
    words = value.split('_')
    value = "".join(word.title() for word in words if word)
    return f"{value[0].lower()}{value[1:]}"


class CustomBaseModel(BaseModel):
    class Config:
        alias_generator = snake_to_camel_case
        extra = Extra.forbid
        allow_population_by_field_name = True


class Author(CustomBaseModel):
    first_name: constr(min_length=1, max_length=20, strip_whitespace=True)
    last_name: constr(min_length=1, max_length=20, strip_whitespace=True)
    display_name: constr(min_length=1, max_length=25) = None

    @validator('display_name', always=True)
    def validate_display_name(cls, value: str, values: dict) -> str:
        if not value in values and 'first_name' in values and 'last_name' in values:
            first_name = values.get('first_name')
            last_name = values.get('last_name')
            return f'{first_name} {last_name[0].upper()}'
        return value


class Link(CustomBaseModel):
    name: constr(min_length=5, max_length=25)
    url: AnyHttpUrl


class Post(CustomBaseModel):
    byline: conlist(item_type=Author, min_items=1)
    title: constr(min_length=10, max_length=50, strip_whitespace=True)
    sub_title: constr(min_length=20, max_length=100, strip_whitespace=True) = None
    body: constr(min_length=100)
    links: List[Link] = []

    @validator('title')
    def validate_title(cls, value):
        return value and value.title()
