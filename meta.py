from gpgauth import GPGAuthSessionWrapper

from requests.utils import dict_from_cookiejar


class PassboltAPIEndpoint:
    def __init__(self, apiManager):
        self.manager = apiManager


class PassboltAPIError(AssertionError):
    pass


from passboltapi.auth import PassboltAuthAPI
from passboltapi.groups import PassboltGroupsAPI
from passboltapi.resources import PassboltResourcesAPI
from passboltapi.users import PassboltUsersAPI


class PassboltAPI:
    def __init__(self, apiContext={}):
        self.apiContext = apiContext
        self.uri = self.apiContext['uri']
        self.verifyCert = self.apiContext['verifyCert']

        # Initialize the endpoints
        self.auth = PassboltAuthAPI(self)
        self.resources = PassboltResourcesAPI(self)
        self.users = PassboltUsersAPI(self)
        self.groups = PassboltGroupsAPI(self)

        # Initialize a null session for now, it will be populated by #authenticate()
        self.session = None

        # Initialize a csrfToken, for now null
        self.csrfToken = None

    def setURI(self, uri):
        self.uri = uri

    def setVerifyCert(self, verifyCert):
        self.verifyCert = verifyCert

    """
    Perform the GPGAuth authentication against the server. Returns True if the authentication is successful,
    False otherwise.
    """
    def authenticate(self, keyring, userFingerprint, serverFingerprint):
        self.session = GPGAuthSessionWrapper(
            gpg=keyring,
            server_url=self.uri,
            user_fingerprint=userFingerprint,
            verify=self.verifyCert
        )

        assert self.session.server_fingerprint == serverFingerprint
        self.session.authenticate()

        return self.session.is_authenticated_with_token

    def buildURI(self, path):
        return '{}/{}'.format(self.uri, path)

    def __buildHeaders(self):
        baseHeaders = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        if self.csrfToken:
            baseHeaders['X-CSRF-TOKEN'] = self.csrfToken
        return baseHeaders

    def __updateCSRFToken(self):
        self.csrfToken = dict_from_cookiejar(self.session.cookies)['csrfToken']

    def __handleResponse(self, response):
        if response.status_code == 200:
            return response.json()['body']
        else:
            self.logger.error('Failed to execute request on Passbolt')
            self.logger.debug(response)
            raise PassboltAPIError(response)

    def get(self, uri, params={}, data={}):
        response = self.session.get(
            uri,
            params=params,
            data=data,
            headers=self.__buildHeaders(),
            verify=self.verifyCert
        )
        self.__updateCSRFToken()
        return self.__handleResponse(response)

    def post(self, uri, params={}, data={}):
        response = self.session.post(
            uri,
            params=params,
            data=data,
            headers=self.__buildHeaders(),
            verify=self.verifyCert
        )
        self.__updateCSRFToken()
        return self.__handleResponse(response)

    def put(self, uri, params={}, data={}):
        response = self.session.put(
            uri,
            params=params,
            data=data,
            headers=self.__buildHeaders(),
            verify=self.verifyCert
        )
        self.__updateCSRFToken()
        return self.__handleResponse(response)

    def delete(self, uri, params={}, data={}):
        response = self.session.delete(
            uri,
            params=params,
            data=data,
            headers=self.__buildHeaders(),
            verify=self.verifyCert
        )
        self.__updateCSRFToken()
        return self.__handleResponse(response)
