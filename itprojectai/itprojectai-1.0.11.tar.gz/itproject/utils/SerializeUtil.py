import joblib

"""序列化/反序列化工具"""


def serialize(model, filename):
    """序列化模型exp：serialize(model,"aura_joblib.lr")"""
    joblib.dump(value=model, filename=filename)


def deserialize(filename):
    """反序列化exp：deserialize("aura_joblib.lr")"""
    return joblib.load(filename=filename)
