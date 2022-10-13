# # Copyright (c) 2022 Shapelets.io
# # 
# # This software is released under the MIT License.
# # https://opensource.org/licenses/MIT
# from typing import List, Optional, Union
# from uuid import UUID

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr, AnyUrl, Field
# import uvicorn
# import asyncio


# app = FastAPI()

# class UserProfile(BaseModel):
#     uid: UUID = Field(description="Unique identifier")
#     nickName: str = Field(description="Unique user id")
#     email: Optional[EmailStr] = None
#     firstName: Optional[str] = None 
#     familyName: Optional[str] = None  
#     locale: Optional[str] = None  
#     picture: Optional[bytes] = None  
#     bio: Optional[str] = None  
#     location: Optional[str] = None  
#     url: Optional[AnyUrl] = None



# @app.get("/", response_model=List[UserProfile])
# async def user_list() -> List[UserProfile]:
#     return []

# @app.delete("/", response_model=bool)
# async def delete_all_users():
#     pass 

# @app.post("/checkNickName", description="Checks if the proposed user name already exists", response_model=bool)
# async def check_nickname(nickName: str) -> bool:
#     return True

# @app.get("/me", response_model=UserProfile)
# async def my_details() -> UserProfile:
#     pass 

# @app.get("/{id}", response_model=Optional[UserProfile])
# async def get_user_details(id: int) -> Optional[UserProfile]:
#     pass 

# @app.put("/{id}")
# async def save_user_details(id: int, details: UserProfile):
#     pass 

# @app.delete("/{id}")
# async def delete_user(id: int):
#     pass 

# @app.get("/{id}/groups")
# async def get_user_groups(id: int):
#     pass 

# @app.get("/{id}/principals")
# async def get_user_principals(id: int):
#     pass 





# import threading
# import asyncio 



# class InProcServerOld(uvicorn.Server):

#     def __init__(self, config: uvicorn.Config) -> None:
#         if config is None:
#             raise ValueError("Configuration is required")

#         super().__init__(config)

#     def install_signal_handlers(self) -> None:
#         pass 

#     def __run_in_separate_ev(self):
#         loop = asyncio.new_event_loop()
#         try:
#             asyncio.set_event_loop(loop)
#             return loop.run_until_complete(self.serve())
#         finally:
#             loop.close()        

#     def run_in_thread(self):
#         self.__ev_thread = threading.Thread(target=self.__run_in_separate_ev, daemon=True, name="api-thread")    
#         self.__ev_thread.start()

#     def stop(self, timeout: Optional[float] = None):
#         self.should_exit = True 
#         self.__ev_thread.join(timeout)
#         if self.__ev_thread.is_alive():
#             raise RuntimeError("Unable to stop event loop thread in a timely manner.")

# import functools



# def main3():
#     config = uvicorn.Config(app, port=8000, log_level="debug", reload=True, debug=True)
#     svr = InProcServer()
#     svr.start(config)
#     return svr

# __all__ = ['main3']

