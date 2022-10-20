import zipfile
import shutil
import pylzma
import os

api_url = ""
temp = os.environ["TEMP"]

class DecompressionError(Exception): pass

class TemporaryDirectory():
    def __init__(self, dirname=None, dir=temp, prefix="", suffix="", ignore_cleanup_errors=True):
        """
        Create a temporary directory.

        [dirname]
            default: None
            description: Sets the name of the temporary directory.
        
        [dir]
            default: Temp path
            description: The directory that the temporary directory is created in.
        
        [prefix]
            default: ""
            description: The prefix to the temporary directories name.
            example: (prefix="example-") example-mytempdir
        
        [suffix]
            default: ""
            description: THe suffix to the temporary directories name.
            example: (suffix="-example") mytempdir-exampled
        
        [ignore_cleanup_errors]
            default: True
            description: Choose to ignore any errors when calling the cleanup() function.
        
        [USAGE EXAMPLE]
            temp = damuffin.TemporaryDirectory()

            # Adding Existing Files
            temp.write("./myfile.txt")

            # Creating New Files
            temp.write("newfile.txt", b"Contents to my new file!")
            
            # Adding Directories
            temp.write("./mydir")

            # Removing Temporary Directory
            temp.cleanup()
        """

        dirname = "tmp" + str(os.urandom(7).hex()) if dirname is None else dirname
        self.name = f"{prefix}{dirname}{suffix}"
        self.path = os.path.join(dir, self.name)
        self.__ignore_errors = ignore_cleanup_errors

        os.mkdir(self.path)

    def write(self, path: str, contents=None):
        """
        Add files or directories to temporary directory.

        [path]
            options: <File Path>, <Directory Name>, <File Name>
            decription: Used to add a file or directory to the temporary directory.
            This function can also be used for creating the new files.
        
        [contents]
            default: None
            description: Used to add contents to a new file.
            Requires Type: Bytes
        
        [USAGE EXAMPLE]
            # Adding Existing Files
            temp.write("./myfile.txt")

            # Creating New Files
            temp.write("newfile.txt", b"Contents to my new file!")
            
            # Adding Directories
            temp.write("./mydir") # Path Exists
            temp.write("mydir") # Path Doesn't Exist (Create new directory)
        """

        if not os.path.exists(path):
            if contents is None: os.mkdir(os.path.join(self.path, path)); return
            with open(os.path.join(self.path, path), "wb") as f: f.write(contents); return
        
        temp_path = os.path.join(self.path, os.path.basename(path))
        if os.path.isdir(path):
            os.mkdir(temp_path)
            shutil.copytree(path, temp_path)
        elif os.path.isfile(path):
            shutil.copy2(path, temp_path)
    
    def cleanup(self):
        """
        Used to delete the temporary directory.

        [USAGE EXAMPLE]
            temp = damuffin.TemporaryDirectory()

            temp.cleanup()
        """

        shutil.rmtree(self.path, ignore_errors=self.__ignore_errors)

class CompressionObject:
    def __init__(self, path):
        """
        Create a compression object to quickly compress and decompress files.

        [path]
            description: A path to the file or folder you want to compress or decompress.

        [USAGE EXAPMLE]
            processor = CompressionObject('./myfolder')

            # Compress Path
            processor.compress()

            # Decompress Path
            processor.decompress()
        """

        self.path = path
    
    def compress(self, dictionary=27, remove_old_files=True):
        """
        Compress the path provided.

        [dictionary]
            default: 27 (Highest Compression)
            range: [0 - 27]
            description: Please view pylzma's docs.
                (It's Basically the Compression Level)
        
        [remove_old_files]
            default: True
            description: Delete the old files that were compressed.
        
        [USAGE EXAMPLE]
            processor.compress()
        """

        DaMuffinCompress(self.path, dictionary=dictionary, remove_old_files=remove_old_files)
    
    def decompress(self, remove_old_files=True):
        """
        Decompress the path provided.
        
        [remove_old_files]
            default: True
            description: Delete the old files that were decompressed.
        
        [USAGE EXAMPLE]
            processor.decompress()
        """

        DaMuffinDecompress(self.path, remove_old_files=remove_old_files)

    def get_dictionary(self):
        """
        Get the dictionary level on a compressed file.

        When a file is compressed using this library. Each file
        is given an extension with the dictionary level used to
        compress that file.

        [USAGE EXAMPLE]
            myfile = "./myfile.txt.cmp27"
            new_file = "./newfile.txt"

            processor = CompressionObject(myfile)
            processor2 = CompressionObject(new_file)

            # Use the same compression for myfile on new_file
            processor2.compress(new_file, processor.get_dictionary())
        """

        name, ext = os.path.splitext(self.path)
        extensions = [f".cmp{i}" for i in range(0, 28)]

        if ext not in extensions: return 27
        
        return extensions.index(ext)

class DaMuffinCompress:
    def __init__(self, path, dictionary=27, remove_old_files=True):
        """
        Compresses a file or folder.

        [path]
            description: A path to the file or folder you want to compress.
        
        [dictionary]
            default: 27 (Highest Compression)
            range: [0 - 27]
            description: Please view pylzma's docs.
                (It's Basically the Compression Level)
        
        [remove_old_files]
            default: True
            description: Delete the old files that were compressed.
        
        [USAGE EXAMPLE]
            damuffin.DaMuffinCompress('./myfile.txt')
        """

        if not os.path.exists(path):
            raise FileNotFoundError(f"Path '{path}' does not exist.")
        
        if os.path.isfile(path):
            cmp_path = os.path.join(os.path.pardir(path), f"{os.path.basename(path)}.cmp{dictionary}")

            with open(path, "rb") as raw_file:
                with open(cmp_path, "wb") as cmp_file:
                    cmp_file.write(pylzma.compress(raw_file.read(), dictionary=dictionary))
                
            if remove_old_files:
                os.remove(path)
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    cmp_path = os.path.join(root, f"{file}.cmp{dictionary}")
                    file_path = os.path.abspath(os.path.join(root, file))

                    with open(file_path, "rb") as raw_file:
                        with open(cmp_path, "wb") as cmp_file:
                            cmp_file.write(pylzma.compress(raw_file.read(), dictionary=dictionary))
                    
                    if remove_old_files:
                        os.remove(file_path)

class DaMuffinDecompress():
    def __init__(self, cmp_path, remove_old_files=True):
        """
        Decompresses a file or folder.

        [cmp_path]
            description: A path to the compressed file or folder you want to decompress.
        
        [remove_old_files]
            default: True
            description: Delete the old files that were decompressed.
        
        [USAGE EXAMPLE]
            damuffin.DaMuffinDecompress('./myfile.cmp27')
        """

        name, ext = os.path.splitext(cmp_path)
        if not [f".cmp{i}" for i in range(0, 28)]:
            raise DecompressionError("Expected a compressed file path.")

        if not os.path.exists(cmp_path):
            raise FileNotFoundError(f"Path '{cmp_path}' does not exist.")
        
        if os.path.isfile(cmp_path):
            file_path = os.path.splitext(cmp_path)[0]

            with open(cmp_path, "rb") as cmp_file:
                with open(file_path, "wb") as raw_file:
                    raw_file.write(pylzma.decompress(cmp_file.read()))
                
            if remove_old_files:
                os.remove(cmp_path)
        elif os.path.isdir(cmp_path):
            for root, dirs, files in os.walk(cmp_path):
                for file in files:
                    cmp_path = os.path.join(root, file)
                    file_path = os.path.splitext(cmp_path)[0]

                    with open(cmp_path, "rb") as cmp_file:
                        with open(file_path, "wb") as raw_file:
                            raw_file.write(pylzma.decompress(cmp_file.read()))
                    
                    if remove_old_files:
                        os.remove(cmp_path)

class DaMuffinZip:
    def __init__(self, path, archive_name, dir=temp, level=9, remove_old_files=True):
        """
        Zip a file or folder.

        [path]
            description: Path to the file or folder to zip.
        
        [archive_name]
            description: The name of the zipped file.
        
        [dir]
            default: Temp path
            description: The directory the zip will be created in.
        
        [level]
            default: 9 (Highest Compression)
            description: The level of zip compression.
        
        [remove_old_files]:
            default: True
            description: Removes the old files that were zipped.
        
        [USAGE EXAMPLE]
            # Create temp
            temp = damuffin.TemporaryDirectory()
            temp.write("./myfolder")
            
            # Get the temp path for "myfolder"
            myfolder = os.path.join(temp.path, "myfolder")

            # Compress the folder
            damuffin.compress(myfolder)

            # Zip the folder
            damuffin.DaMuffinZip(temp.path, 'myfolder.zip', level=0)

            # Remove Temporary Directory
            temp.cleanup()
        """

        if not os.path.exists(path):
            raise ValueError(f"Path '{path}' does not exist.")
        
        self.path = path
        self.zip_path = os.path.join(dir, f"{archive_name}.zip")
        self.__level = level

        if os.path.isfile(path):
            self.__file_procedure()

            if remove_old_files:
                os.remove(path)
        elif os.path.isdir(path):
            self.__directory_procedure()
        
            if remove_old_files:
                shutil.rmtree(path)
    
    def __file_procedure(self):
        with zipfile.ZipFile(self.zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=self.__level) as zip_object:
            zip_object.write(self.path, os.path.basename(self.path))
    
    def __directory_procedure(self):
        items = os.walk(self.path)
        with zipfile.ZipFile(self.zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=self.__level) as zip_object:
            for root, dirs, files in items:
                for file in files:
                    zip_object.write(os.path.join(root, file), 
                            os.path.relpath(os.path.join(root, file), 
                                            os.path.join(self.path, '..')))