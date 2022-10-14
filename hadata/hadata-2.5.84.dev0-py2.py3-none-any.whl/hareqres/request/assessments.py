from datetime import date

from pydantic import BaseModel


class QuestionSortOrder(BaseModel):
    assessmentQnaId: str
    sortOrder: str


class AssessmentCreation(BaseModel):
    type: str
    title: str
    startDate: date
    endDate: date
    description: str


class AssessmentStatusChange(BaseModel):
    assessment_id: str
    isActive: bool


class AssessmentUserRequest(BaseModel):
    firstName: str
    lastName: str
    email: str
    assessmentId: str
    enabled: bool
    score: int
    status: str


class AssessmentUserAddRequest(BaseModel):
    email: str
    assessmentId: str
    enabled: bool
    score: int
    status: str


class AssessmentUserStatusRequest(BaseModel):
    assessmentUserId: str
    enabled: bool


class UserAssessmentMarkedRequest(BaseModel):
    assessmentUserId: str
    marked: bool


class UserAssessmentQNAMarkedRequest(BaseModel):
    assessmentUserQnaId: str
    isCorrect: bool
    personalNotes: str
