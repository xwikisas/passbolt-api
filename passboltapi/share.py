from .meta import PassboltAPIEndpoint


class PassboltShareAPI(PassboltAPIEndpoint):
    def put(self, resourceID, data=None):
        return self.manager.put(
            self.manager.buildURI('/share/resource/{}.json'.format(resourceID)),
            data=data,
            params={'api-version': 'v1'}
        )
