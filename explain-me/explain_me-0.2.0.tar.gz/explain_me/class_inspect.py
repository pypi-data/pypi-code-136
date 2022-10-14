import inspect
from typing import Any


class ClassDiagram:
    kelas: Any
    koneksi_kelas: Any
    
    def __init__(self, kelas: Any = None) -> None:
        self.kelas = kelas
        self.koneksi_kelas = []
    
    
    @property
    def kelas_name(self):
        return self.kelas.__name__
    
    @property
    def kelas_annotation(self):
        if hasattr(self.kelas, '__annotations__'):
            return self.kelas.__annotations__
        
        return {}
    
    def extract_tipename(self, value):
        try:
            tipename = value.__name__
        except:
            tipename = str(value).replace('.', '_')
            
        return tipename
    
    def get_parent(self):
        fields = []
        
        for kelas in self.kelas.__bases__:
            if kelas == object:
                continue
            
            clsname = kelas.__name__
            field = f"{clsname} <|.. {self.kelas_name} : Inherit"
            
            fields.append(field)
        
        return fields
    
        
    def to_fuction(self):
        method_list = inspect.getmembers(self.kelas, predicate=inspect.isfunction)

        fields = []
        
        for key, func in method_list:
            
            field = f"+ {key}()"
            fields.append(field)
            
        return fields
        
    def to_field(self):
        fields = []
        
        
        for key, value in self.kelas_annotation.items():
            tipename = self.extract_tipename(value)
                
            field = f"+ {key} {tipename} "
            fields.append(field)
        
        return fields
    
    
    def to_connection(self):
        connection = {}
        
        for key, value in self.kelas_annotation.items():
            tipename = self.extract_tipename(value)
            if not inspect.isclass(value):
                continue
            if issubclass(value, (str, int, float, list, tuple, set)):
                continue
            
            connection[tipename] = self.kelas_name
            
        fields = []
        for tipename, key in connection.items():
            field = f"{tipename} --|> {key} : Dependend"
            
            fields.append(field)
            
        
        return fields + self.get_parent()
    
    
    
    def __call__(self):        
        fields = self.to_field() + self.to_fuction()
        if len(fields) == 0:
            return ''
        
        content_field = "{\n" + "\n".join(fields) + "\n}"
        
        content = '''
{connection}
class {name}{field}
        '''
        
        return content.format(
            name=self.kelas_name,
            field=content_field,
            connection="\n".join(self.to_connection())
        )
    
    


class Parent:
    slow: int
    
    def slowman(self):
        pass



class CHCC(Parent):
    asd: bool


class TestChild:
    fvs: str
    
    def runner(self):
        pass



class TestSS:
    nama: str
    blues: int
    
    child: TestChild
    
    
    def globe(self):
        pass


if __name__ == '__main__':
    
        
        
    test = ClassDiagram(TestSS)
    child = ClassDiagram(TestChild)
    parent = ClassDiagram(Parent)
    ch = ClassDiagram(CHCC)
    print(
        test(),
        child(),
        parent(),
        ch()
    )



