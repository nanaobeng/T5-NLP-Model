import pydantic as _pydantic

from typing import Union


class Translate(_pydantic.BaseModel):
    source_language: Union[str, None] = None
    target_language: Union[str, None] = None
    text: str
