

def methodwrapper(func):
    import pythonagent.agent as agent
    _agent = agent.get_agent_instance()
    print(func.__module__)
    fqm = str(func.__module__) +"."+ str(func.__name__)
    bt = _agent.get_current_bt()
    #bt = "000001"
    def inner(*args, **kwargs):
        try:
            _agent.method_entry(bt, fqm)
        except Exception as e:
            print(e)
        rc = func(*args, **kwargs)
        try:
            _agent.method_exit(bt, fqm, 200)
        except Exception as e:
            print(e)
        return rc
        
    return inner
