from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional


class ResolutionRule:
    tenant_id: str
    default_attributes: list[str]
    custom_attributes: list[str]
    match_strategy: str
