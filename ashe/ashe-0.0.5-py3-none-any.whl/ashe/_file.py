def read(file_path: str) -> str:
    with open(file_path, "r") as f_read:
        return f_read.read()


def write(file_path: str, file: str) -> None:
    with open(file_path, "w") as f_write:
        f_write.write(file)
