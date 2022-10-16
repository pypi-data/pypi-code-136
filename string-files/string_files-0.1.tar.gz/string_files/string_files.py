def get_strings(filename, amount: int, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as f:
        lines = f.readlines()
        result = []
        for i in range(amount):
            try:
                line = lines.pop(0)
                line = line.replace('\n', '')
                result.append(line)
            except:
                break
    return result

def get_strings_rewrite(filename, amount: int, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as f:
        lines = f.readlines()
        result = []
        for i in range(amount):
            try:
                line = lines.pop(0)
                line = line.replace('\n', '')
                result.append(line)
            except:
                break
    with open(filename, 'w', encoding=encoding) as f:
        for line in lines:
            f.write(line)
    return result