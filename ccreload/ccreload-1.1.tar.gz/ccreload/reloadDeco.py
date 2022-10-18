from .autoreload import run_with_reloader
from decorator import decorator

demo = f'''
      #################################
      #  from ccreload import creload #
      #                               #
      #  @creload                     #
      #  def main():                  #
      #      print('test')            #
      #################################
        '''

@decorator
def ccreload(func,*args,**kwargs):
    run_with_reloader(func)

