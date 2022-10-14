
from .option import Option
import numpy as np

    
        
class Model:
    
    def __init__(self) -> None:
        raise Exception("Cannot instanciate")
    
    def predict(self, image: np.ndarray)->Option:
        raise NotImplementedError()
        
    
    def for_static_images(*args, **kwargs)->"Model":
        raise NotImplementedError()
    
    def for_videos(*args, **kwargs)->"Model":
        raise NotImplementedError()
               
               
               
class ModelOutput:
    
    def __init__(self) -> None:
        raise Exception("Cannot instanciate")    
    
    def to_dict(self)->dict:
        raise NotImplementedError()           
        
    def draw(self, original_image:np.ndarray)->None:
        raise NotImplementedError()           
        
          