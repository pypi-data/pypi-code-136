from pydantic import BaseModel, constr


class UserInfo(BaseModel):
    user_id: constr(strict=True, min_length=1)
    email: constr(strict=True, min_length=1)
