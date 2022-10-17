from .autoreload import run_with_reloader
from decorator import decorator

demo = f'''
        {'#'*50}
        from ccreload import creload
        
        @creload
        def main():
            print('test')
        {'#'*50}
        '''

@decorator
def ccreload(func,*args,**kwargs):
    run_with_reloader(func)

