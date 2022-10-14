class Option:
    
    def __init__(self, data, msg=None) -> None:
        self.data = data
        self.msg = msg
    
    def is_ok(self)->bool:
        return not self.data is None 
    
    def wrap(func):
        
        def wrapper(*args, **kwargs):
            
            data = None
            msg = None
            
            try:
                data = func(*args, **kwargs)
            
            except Exception as e:
                msg = str(e)

            if isinstance(data, Option):
                return data
                
            return Option(data=data, msg=msg)
        
        return wrapper