from datetime import datetime


def write_diary():
    """ Write your thoughts into the diary file """
    with open('diary', 'a+') as f:
        note = input('Привет! Напиши о чем думаешь:\n')
        f.write(f'{datetime.now().isoformat()}\n{note}\n\n')

    with open('diary', 'r') as f:
        print(f.read())


def read_diary():
    with open('diary', 'r') as f:
        print(f.read())


if __name__ == "__main__":
    diary()
    read_diary()
