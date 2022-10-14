from typing import Optional, List

from pydantic import BaseModel


class QuestionAnswerEditRequest(BaseModel):
    job_id: Optional[str]
    question: Optional[str]
    answer: Optional[str]
    skill_id: Optional[str]
    subskill_1_id: Optional[str]
    subskill_2_id: Optional[str]
    subskill_3_id: Optional[str]
    level_id: Optional[str]
    question_type: Optional[str]
    question_theme: Optional[str]
    time: Optional[str]
    points: Optional[int]
    media_question: Optional[bool]
    media_extension: Optional[str]
    file_encoded: Optional[str]
    roles: Optional[List[str]]


class QuestionSearch(BaseModel):
    questionTitle: Optional[str] = None
    skillId: Optional[str] = None
    levelId: Optional[str] = None
    subskill1Id: Optional[str] = None
    subskill2Id: Optional[str] = None
    subskill3Id: Optional[str] = None
    roleId: Optional[str] = None
