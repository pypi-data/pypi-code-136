class AboutMe:
    
    def __init__(self) -> None:
        pass 
    
    def get_firstname(self) -> str:
        return "John"
    
    def get_surname(self) -> str:
        return "Robert"
    
    def get_full_name(self) -> str:
        return f"{self.get_firstname()} {self.get_surname} "