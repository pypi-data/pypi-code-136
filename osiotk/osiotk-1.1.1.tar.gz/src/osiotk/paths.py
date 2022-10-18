from collections import defaultdict as _defaultdict
def filetree(__ft: str,indent:int=4) -> list[str]:
    dirlog, results = _defaultdict(list[str]), []
    for line in (line for line in __ft.splitlines(keepends=False) if line):
        offset, path = len(line) - len(line.lstrip()), line.strip()
        dirlog[offset].append(path)
        while offset > 0:
            if dirlog[offset - indent]:
                path = f"{dirlog[offset-indent][-1]}/{path}"
            offset -= indent
        results.append(path)
    return results