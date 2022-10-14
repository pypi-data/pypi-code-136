from sqlmodel import Session


from .sqlmodels import *

def doit(engine):
    with Session(engine) as session:
        u=TapirUsers(user_id=123,email='a@lkjb.com')
        n=TapirNicknames(nick='aaa', user=n)
        session.add(u)
        session.commit()

        session.refresh(u)
        print("created user: ", u)
