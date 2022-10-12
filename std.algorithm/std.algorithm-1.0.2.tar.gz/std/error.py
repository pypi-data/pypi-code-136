import sys

class __LINE__:

    def __repr__(self):
        try:
            raise Exception
        except:
            return str(sys.exc_info()[2].tb_frame.f_back.f_lineno)

 
__LINE__ = __LINE__()
