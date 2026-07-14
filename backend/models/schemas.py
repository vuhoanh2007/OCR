from pydantic import BaseModel, Field
from typing import Optional

class OCRData(BaseModel):
    id: str = Field(default="")
    name: str = Field(default="")
    dob: str = Field(default="")
    gender: str = Field(default="")
    nationality: str = Field(default="Việt Nam")
    origin: str = Field(default="")
    address: str = Field(default="")
    issue_date: str = Field(default="")
    expire_date: str = Field(default="")

class BackOCRData(BaseModel):
    characteristics: str = Field(default="")
    issue_authority: str = Field(default="")
    qr_data: str = Field(default="")
    mrz: str = Field(default="")

class OCRResponse(BaseModel):
    success: bool
    confidence: float
    processing_time: float
    data: OCRData | BackOCRData | dict
    error: Optional[str] = None
