import os

def createNewFile(path):
    createNewPath(os.path.dirname(path))

    try:
        os.mknod(path)
    except:
        with open(path, 'w') as _:
            ...


def createNewPath(basedir):
    if not os.path.exists(basedir):
        os.makedirs(basedir)


class Text:

    def __init__(self, path, encoding="utf-8", **kwargs):
        try:
            self.file = open(path, "r+" if os.path.isfile(path) else "w+", encoding=encoding)
        except PermissionError: 
            self.file = open(path, "r", encoding=encoding)
        except FileNotFoundError:
            createNewFile(path)
            self.file = open(path, "w+", encoding=encoding)

        self.rewind()
        
        if kwargs.get('strip'):
            self.rstrip = self.lstrip = True
        else:
            self.rstrip = kwargs.get('rstrip', True)
            self.lstrip = kwargs.get('lstrip', False)

    def __del__(self):
        self.close()

    def close(self):
        self.file.close()
        
    def __iter__(self):  # Get iterator object on iter
        return self

    def __next__(self):
        while True:
            line = self.file.readline()
            if not line:
                self.rewind()
                raise StopIteration
            
            if self.lstrip:
                line = line.lstrip()
                            
            if self.rstrip:
                line = line.rstrip()
            else:
                if line.endswith('\n'):
                    line = line[:-1]
                
            if not self.lstrip or not self.rstrip or line:
                return line

    def prepend(self, s):
        '''
        prepend = append before the list;
        '''
        self.rewind()

        content = self.file.read()
        self.write(s)
#         self.file.seek(0, 2)
        self.file.write(content)
        self.file.flush()

    def append(self, s, end_of_line='\n'):
        self.end()

        if type(s) == str:
            self.file.write(s + end_of_line)
        else:
            for s in s:
                self.file.write(s + end_of_line)
        self.file.flush()

    def insert(self, index, s):
        if index < 0:
            self.end()
            index = -index - 1
            offset = self.file.tell() - 1
            while index > 0:
                index -= 1
                offset -= 1
                while True:
                    offset -= 1
                    _offset = self.file.seek(offset, os.SEEK_SET)
                    assert _offset == offset
                    char = self.file.read(1)
#                     print('char =', char)
                    if char[0] == '\n' or char[0] == '\r':
                        break
        else:
            self.rewind()
            offset = self.f.tell()
            while index > 0:
                index -= 1
                while True:
                    offset += 1
                    _offset = self.f.seek(offset, os.SEEK_SET)
                    assert _offset == offset
                    char = self.f.read(1)
#                     print('char =', char)
                    if char[0] == '\n' or char[0] == '\r':
                        break

        current_pos = self.file.tell()
        assert current_pos == offset + 1

        rest = self.file.read()
        self.file.seek(current_pos, os.SEEK_SET)

        if type(s) == str:
            self.file.write(s + '\n')
        else:
            for s in s:
                self.file.write(s + '\n')

        self.file.write(rest)

        self.file.flush()

    def __getitem__(self, index):
        if index < 0:
            self.end()
            index = -index
            offset = self.f.tell() - 1
            while index > 0:
                index -= 1
                offset -= 1
                while True:
                    offset -= 1
                    _offset = self.f.seek(offset, os.SEEK_SET)
                    assert _offset == offset
                    char = self.f.read(1)
    #                     print('char =', char)
                    if char == '\n' or char == '\r':
                        break
        else:
            self.rewind()
            offset = self.f.tell()
            while index > 0:
                index -= 1
                while True:
                    offset += 1
                    _offset = self.f.seek(offset, os.SEEK_SET)
                    assert _offset == offset
                    char = self.f.read(1)
#                     print('char =', char)
                    if char == '\n' or char == '\r':
                        break
        current_pos = self.f.tell()

        self.f.seek(current_pos, os.SEEK_SET)

        return self.f.readline().strip()

    def write(self, s):
        self.rewind()

        if type(s) == str:
            self.file.write(s + '\n')
        else:
            for s in s:
                self.file.write(str(s) + '\n')
        self.file.truncate()
        self.file.flush()

    def writelines(self, s):
        self.rewind()

        for s in s:
            self.file.write(str(s) + '\n')
            
        self.file.truncate()
        self.file.flush()
        
    def clear(self):
        self.rewind()
        self.file.write('')
        self.file.truncate()
        self.file.flush()

    def rewind(self):
#         skip_byte_order_mark
        self.file.seek(0, os.SEEK_SET)
        byteOrderMark = self.file.read(1)
        if byteOrderMark and ord(byteOrderMark) != 0xFEFF:
            self.file.seek(0, os.SEEK_SET)        

    def end(self):
        self.file.seek(0, os.SEEK_END)

    def collect(self):
        self.rewind()

        arr = []
        for line in self:
            arr.append(line)
        return arr

    def remove(self, value=None, index=None):
        arr = self.collect()
        if index is None:
            if value in arr:
                arr.remove(value)
                self.write(arr)
        else:
            del arr[index]
            self.write(arr)

    def removeDuplicate(self):
        arr = []
        st = set()
        for s in self.collect():
            if s not in st:
                st.add(s)
                arr += [s]

        self.write(arr)

    def read(self):
        return self.file.read()
    
    def tell(self):
        return self.file.tell()
    
    @property
    def size(self):
        tell = self.tell()
        self.end()
        size = self.file.tell()
        self.file.seek(tell, os.SEEK_SET)        
        return size
        
    def endswith(self, end):
        self.end()
        size = len(end)
        offset = self.file.tell() - size
        if offset < 0:
            return False
        
        _offset = self.file.seek(offset, os.SEEK_SET)
        assert _offset == offset
        char = self.file.read(size)        
        return char == end

    def readlines(self): 
        return [s for s in self]
    
    def readline(self):
        try: 
            return next(self)
        except StopIteration:
            return ''
    
    def writelines(self, array): 
        self.rewind()

        for s in array:
            self.file.write(str(s) + '\n')

        self.file.truncate()
        self.file.flush()

    def find(self, regex, bool=True):
        import re
        for i, line in enumerate(self):
            if re.match(regex, line):
                if bool:
                    return True
                return i
        if bool:
            return False
        else:
            return -1
    