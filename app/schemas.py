from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    date_of_birth: date
    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=20)
    course: str = Field(min_length=1, max_length=100)
    address: str | None = Field(default=None, max_length=250)
    enrollment_date: date


class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    date_of_birth: date | None = None
    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=20)
    course: str | None = Field(default=None, min_length=1, max_length=100)
    address: str | None = Field(default=None, max_length=250)
    enrollment_date: date | None = None


class StudentResponse(StudentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)