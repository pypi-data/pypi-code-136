from pyclbr import readmodule
import os
import threading 
    
    
def application_callable_pro(self, application, instance, environ, start_response):
    stack = inspect.stack()
    temp={}
    the_method_called = stack[3][0].f_code.co_name
    request = Request(environ)
    prof = cProfile.Profile()
    prof.enable()
    bt = self.start_business_transaction(request.full_path, '')
    self.agent.logger.debug("Modulename: WSGI intercepto class || bt value is :{0}".format(bt))
    method = self.agent.method_entry(bt,the_method_called)

    try:
        self.agent.logger.info("Modulename: WSGI interceptor class || request is :{0} || request path is {1} || query_string: {2} || host: {3} ".format(request,(request.path,request.query_string,request.host)))
    except:
        pass

    try:
        response = application(instance, environ, self._make_start_response_wrapper(start_response))
        self.agent.logger.info("Modulename: WSGI interceptor class || response is :{0}".format(response))

    except:
        with self.log_exceptions():
            if bt:
                bt.add_exception(*sys.exc_info())
        raise
    finally:
        method = the_method_called
        self.agent.method_exit(bt,method)
        self.end_business_transaction(bt)
        prof.disable()
        prof.print_stats()
        p = pstats.Stats(prof)
        #client application path
        client_app_root = os.path.dirname(sys.argv[0])

        for k,v in p.stats.items():

            if client_app_root in k[0]:
                module = k[0]
                print("module:-", k[0])
                module_path = os.path.split(os.path.abspath(module))[0]
                modulefullname  = os.path.split(os.path.abspath(module))[1]
                module_name = modulefullname.split('.')[0]
                methodname = k[-1]
                print('module path:-', module_path)
                print('module name:-', module_name)
                print('method name:- ',k[-1])
                print('Total call:- ',v[1])
                print('Response time of method:-',v[3])
                mod = readmodule(module_name, path=[module_path])
                li = []
                for k, v in mod.items():
                    li.append(k)
                    methods = v.methods.items()
                    lk = []
                    for method, lineno in methods:
                        lk.append(method)
                    li.append(lk)
                count=0
                for i in li:
                    count +=1
                    if type(i)==str:
                        pass
                    else:
                        for j in i:
                            if j == methodname:
                                print("classname:-",li[count-2])
                            else:
                                pass
    return response

def application_callable(self, application, instance, environ, start_response):
    stack = inspect.stack()
    temp={}
    the_method_called = stack[3][0].f_code.co_name
    request = Request(environ)
    bt = self.start_business_transaction(request.full_path, '')
    self.agent.logger.debug("Modulename: WSGI interceptor class || bt value is :{0}".format(bt))
    method = self.agent.method_entry(bt,the_method_called)

    try:
        self.agent.logger.info("Modulename: WSGI interceptor class || request is :{0} || request path is {1} || query_string: {2} || host: {3} ".format(request,(request.path,request.query_string,request.host)))
    except:
        pass

    try:
        response = application(instance, environ, self._make_start_response_wrapper(start_response))
        self.agent.logger.info("Modulename: WSGI interceptor class || response is :{0}".format(response))

    except:
        with self.log_exceptions():
            if bt:
                bt.add_exception(*sys.exc_info())
        raise
    finally:
        method = the_method_called
        self.agent.method_exit(bt,method)
        self.end_business_transaction(bt)

    return response
