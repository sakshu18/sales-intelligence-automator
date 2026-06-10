from pydantic import BaseModel, Field
from typing import List


class SalesBrief(BaseModel):
    company_name: str
    company_overview: str
    core_product_service: str
    target_customer: str
    b2b_qualified: bool
    sales_questions: List[str]