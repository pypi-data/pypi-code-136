import posixpath
from io import BytesIO
import logging


log = logging.getLogger(__name__)


class Sharepoint:
    def __init__(self, conf, site_name):
        self.tenant_name = conf.tenant_name
        self.tenant_id = conf.tenant_id
        self.client_id = conf.client_id
        self.key = conf.key
        self.thumbprint = conf.thumbprint
        self.site_name = site_name
        self.session = None

    def connect(self, force=False):
        """
        connects to office 365 and sets up the session.  If a session
        already exists, we reuse that session.  To force the creation
        of a new session, set force=True.

        Args:

            force (bool): set this flag to True if you want to force
                          return a fresh session.
        """
        import adal
        from office365.runtime.auth.token_response import TokenResponse
        from office365.sharepoint.client_context import ClientContext
        if self.session and not force:
            return self.session
        sharepoint_base_url = f'https://{self.tenant_name}.sharepoint.com'
        site_url = f'{sharepoint_base_url}/sites/{self.site_name}'
        authority = f'https://login.microsoftonline.com/{self.tenant_id}'
        app = adal.AuthenticationContext(authority)
        token_json = app.acquire_token_with_client_certificate(
            sharepoint_base_url,
            self.client_id,
            self.key,
            self.thumbprint,
        )
        self.session = ClientContext(site_url).with_access_token(
            lambda: TokenResponse.from_json(token_json)
        )
        return self.session

    def ensure(self, d):
        """
        ensures that d exists
        """
        from office365.sharepoint.folders.folder import Folder
        session = self.connect()
        pieces = d.split(posixpath.sep)[3:]
        s: Folder = session.web.root_folder
        s = s.expand(['Folders'])
        for x in pieces:
            found = False
            s = s.get().execute_query()
            for y in s.folders:
                if y.name == x:
                    found = True
                    s = y
                    break
            if not found:
                log.info('creating folder %s in %s', x, s.serverRelativeUrl)
                s = s.folders.ensure_folder_path(x).execute_query()
        return s

    def upload(self, buff, destination, retry_401=True):
        """
        uploads a BytesIO to the destination path
        Args:
            buff (BytesIO): the data to upload
            destination (str): the location in sharepoint where the file will
                               be stored
            retry_401 (bool): defaults to true.  If specified as true,
                              and we receive a 401 error from the download
                              operation, we will retry exactly once
                              to see if refreshing the token overcomes the 401
                              error
        """
        from office365.sharepoint.folders.folder import Folder
        from office365.runtime.client_request_exception import ClientRequestException
        destination = destination.replace('Documents', 'Shared Documents')
        d = posixpath.dirname(destination)
        base = posixpath.basename(destination)
        destination = posixpath.join('/sites', self.site_name, d)
        folder: Folder = self.ensure(destination)
        buff.seek(0)
        log.info(f'uploading %s => %s', base, destination)
        try:
            folder.upload_file(base, buff.getvalue()).execute_query()
        except ClientRequestException as ex:
            if ex.response.status_code == 401 and retry_401:
                # we can get a 401 when our token expires, set
                # session to None here so that we reconnect on the
                # retry
                self.session = None
                return self.upload(buff, destination, False)
            raise

    def download(self, filename, retry_401=True):
        """
        Downloads the specified path into a BytesIO buffer

        Args:
            filename (str): the name of the file to download
            retry_401 (bool): defaults to true.  If specified as true,
                              and we receive a 401 error from the download
                              operation, we will retry exactly once
                              to see if refreshing the token overcomes the 401
                              error
        """
        from office365.runtime.client_request_exception import ClientRequestException
        source = filename.replace('Documents', 'Shared Documents')
        source = posixpath.join('/sites', self.site_name, source)
        session = self.connect()
        f = session.web.get_file_by_server_relative_path(source)
        log.info('downloading %s from %s', filename, self.site_name)
        buff = BytesIO()
        try:
            f.download(buff).execute_query()
        except ClientRequestException as ex:
            if ex.response.status_code == 401 and retry_401:
                # we can get a 401 when our token expires, set
                # session to None here so that we reconnect on the
                # retry
                self.session = None
                return self.download(filename, False)
            raise
        buff.seek(0)
        return buff

    def upload_dataframes(self, filename, *args):
        """
        provide arguments as filename, df1, sheet_name1, df2, sheet_name2, ...
        """
        import pandas as pd
        n = len(args)
        buff = BytesIO()
        with pd.ExcelWriter(buff) as f:
            for x in range(0, n, 2):
                df = args[x]
                sheet_name = args[x + 1]
                df.to_excel(f, sheet_name=sheet_name)
        self.upload(buff, filename)

    def upload_dataframe_csv(self, filename, df, **kwargs):
        """
        provide arguments as filename, df.  kwargs will be passed through
        to the dataframe `to_csv` function.
        """
        buff = BytesIO()
        df.to_csv(buff, **kwargs)
        self.upload(buff, filename)

    def download_dataframe(self, filename, engine='openpyxl', **kwargs):
        """
        downloads the file from sharepoint and provides it to the caller
        as a dataframe
        """
        import pandas as pd
        buff = self.download(filename)
        df = pd.read_excel(io=buff)
        return df
