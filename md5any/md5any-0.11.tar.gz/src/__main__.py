import sys

from .error import MD5AnyErrorCode
from .process import Hash

def main():
    try:
        targets = sys.argv[1:]
        if len(targets) < 1:
            raise MD5AnyErrorCode("Bad target")
        [Hash.test(target) for target in targets]
        for target in targets:
            print(Hash(target).absrtact, target)
    except MD5AnyErrorCode as e:
        print(e)

if __name__ == '__main__':
    main()