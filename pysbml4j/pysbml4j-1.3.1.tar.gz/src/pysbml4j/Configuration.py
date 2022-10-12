class Configuration(object):
    #_server=None
    #_user=None

    def __init__(self, server="http://localhost", port=8080, application_context="/sbml4j", user="sbml4j"):
        self._server = server
        self._port = port
        self._application_context = application_context
        #print("Server is: " + self._server + ":" + str(self._port) + self._application_context)
        # Set headers
        self._headers = {'Accept':'application/json', 'user':user}
        self._isInSync = False
    @property
    def isInSync(self):
        return self._isInSync

    @isInSync.setter
    def isInSync(self, value):
        self._isInSync = value

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, value):
        self._server=value
        self._isInSync=False

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        self._port = value
        self._isInSync=False

    @property
    def application_context(self):
        return self._application_context

    @application_context.setter
    def application_context(self, value):
        self._application_context = value
        self._isInSync=False

    @property
    def user(self):
        return self._headers['user']
    @user.setter
    def user(self, value):
        self._headers['user'] = value
        self._isInSync=False

    @property
    def headers(self):
        return self._headers

    @property
    def accept(self):
        return self._headers['Accept']
    @accept.setter
    def accept(self, value):
        self._headers['Accept'] = value

    @property
    def url(self):
        url = self._server + ":" + str(self._port) + self._application_context
        return url
    #@property
    #def content_type(self):
    #    return self._headers['Content-Type']
    #@content_type.setter
    #def content_type(self, value):
    #    self._headers['Content-Type'] = value


    def __str__(self):
        return "Server: {}:{}{} with headers: {}".format(self._server, self._port, self._application_context, self._headers)
