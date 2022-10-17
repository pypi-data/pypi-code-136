from fastapi import HTTPException

def ajwt_token_finder(**kwargs):
    return str(kwargs["Authorization"]).replace("Bearer ", "")

def ajwt_exception_handler(code: int, msg: str):
    raise HTTPException(status_code=code, detail=msg)

def create_fastapi_template():
    token_finder = ajwt_token_finder
    exception_handler = ajwt_exception_handler
    return token_finder, exception_handler