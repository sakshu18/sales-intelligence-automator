from pydantic import BaseModel, Field
from typing import List


class ICPProfile(BaseModel):

    target_roles: List[str] = Field(
        default_factory=list
    )

    pain_points: List[str] = Field(
        default_factory=list
    )

    buying_signals: List[str] = Field(
        default_factory=list
    )

    trigger_events: List[str] = Field(
        default_factory=list
    )

    tech_stack_signals: List[str] = Field(
        default_factory=list
    )

    qualification_score: int = 0

    icp_match_reason: str = (
        "No ICP analysis available."
    )