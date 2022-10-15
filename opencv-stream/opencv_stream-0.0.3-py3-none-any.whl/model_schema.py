
from .option import Option
import numpy as np

    
        
class Model:
    """
    Inherit from the class to define your model
    """
    
    def __init__(self) -> None:
        raise Exception("Cannot instanciate")
    
    def predict(self, image: np.ndarray)->Option:
        raise NotImplementedError()
        
               
               
class ModelOutput:

    """
    Inherit from this class to define your model output\n
    use the to_dict method to generate a json dictionary representation\n
    of you output. (For Apis)

    Use the draw function to define how the output should be drawn onto the screen
    """
    
    def __init__(self) -> None:
        raise Exception("Cannot instanciate")    
    
    def to_dict(self)->dict:
        raise NotImplementedError()           
        
    def draw(self, image:np.ndarray)->None:
        raise NotImplementedError()           
        
          