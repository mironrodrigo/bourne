from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional


class ProfileCreate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = Field(..., regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    phone: Optional[str] = None
    address: Optional[str] = None


class ProfileResponse(ProfileCreate):
    customer_uuid: UUID = Field(default_factory=uuid4)
    custom_attributes: dict = Field(default_factory=dict)
    identifiers: dict = Field(
        default_factory=dict,
        description="Identifiers mapping used to resolute customer ID"
    )