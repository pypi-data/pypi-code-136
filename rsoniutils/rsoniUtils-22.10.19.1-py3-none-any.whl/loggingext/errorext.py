"""
  Common methods are defined here
  for error and exception. 

"""
import traceback
import sys
class ErrorExt(Exception):
      pass

class DefaultException(ErrorExt):
      
      
      def __init__(self, *args):
            if args:
             exc_type, exc_value, exc_tb = sys.exc_info()
             self.message = ' '.join([str(elem) for elem in traceback.format_exception(exc_type, exc_value, exc_tb)]) 
            else:
             self.message = None
        
      def __str__(self):
             return self.message
         
class FileException(ErrorExt):
    def __init__(self, *args):
        try:
            if args:
                self.message = args[0]
            else:
                self.message = None
        except Exception as ex:
                print(f"exception occured {str(ex)}")        
            
    def __str__(self):
        try:
            if self.message:
                return 'File Exception occured, {0} '.format(self.message)
            else:
                return 'File Exception has been raised'
        except Exception as ex:
                print(f"exception occured {str(ex)}") 