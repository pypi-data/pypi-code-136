from typing import Optional, List

from pydantic import BaseModel


class QuestionAnswer(BaseModel):
    id: str
    jobId: str
    question: str
    answer: str
    skillId: Optional[str]
    levelId: Optional[str]
    subskill1Id: Optional[str]
    subskill2Id: Optional[str]
    subskill3Id: Optional[str]
    questionType: str
    questionTheme: Optional[str]
    time: str
    points: int
    mediaQuestion: Optional[bool]
    mediaExtension: Optional[str]
    fileEncoded: Optional[str]
    roles: Optional[List[str]]
