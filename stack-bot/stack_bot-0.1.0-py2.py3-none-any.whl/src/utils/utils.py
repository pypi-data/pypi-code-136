def clear_context(context: dict):
    keys = list(context.keys())
    for k in keys:
        context.pop(k)