def openapi(
        return_class=None, description=None, path_parameters=None, parameters=None, body=None, answer_content=None,
        tags=None
):
    def decorate(f):
        def wrapper(*args, **kwargs):
            if len(args) == 1:
                if args[0] == 'openapi':
                    return {
                        'return_class': return_class,
                        'description': description,
                        'path_parameters': path_parameters,
                        "parameters": parameters,
                        "body": body,
                        "answer_content": answer_content,
                        'tags': tags
                    }
            return f(*args, **kwargs)
        return wrapper
    return decorate
