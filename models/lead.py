from pydantic import BaseModel, HttpUrl
from typing import Optional


class Lead(BaseModel):
    company_name: str
    website_url: Optional[HttpUrl] = None
    location: Optional[str] = None

    @property
    def has_website(self) -> bool:
        return self.website_url is not None