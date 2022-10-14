def label_func1(f):
    return f[:-4].split('_')[-1]
def label_func2(f):
    stage = "N"
    if stage == "S":
        res = f[:-4].split('_')[-2]
    elif stage == "M":
        res = f[:-4].split('_')[-4]
    elif stage == "N":
        res = f[:-4].split('_')[-3]
    elif stage == "T":
        res = f[:-4].split('_')[-1]
    return res