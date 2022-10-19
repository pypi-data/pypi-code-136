
class StringBuilder:
     _file_str = ''

     def __init__(self):
         self._file_str = ''

     def Append(self, str):
         self._file_str += str

     def AppendLine(self, str):
        self._file_str += str  
        self._file_str += '\n' 
     
     def ToString(self):
        return self._file_str 

     def __str__(self):
         return self._file_str


#sb= StringBuilder()
#sb.AppendLine("hello")
#sb.AppendLine("aasdfasdf")
#print(sb.ToString())