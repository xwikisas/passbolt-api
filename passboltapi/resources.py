from .meta import PassboltAPIEndpoint


class PassboltResourcesAPI(PassboltAPIEndpoint):
    def get(self, resourceID=None, params={}):
        if resourceID:
            return self.manager.get(
                self.manager.buildURI('/resources/{}.json'.format(resourceID))
            )
        else:
            return self.manager.get(
                self.manager.buildURI('/resources.json'),
                params=params
            )

    # Uses API v2
    def post(self, data=None):
        return self.manager.post(
            self.manager.buildURI('/resources.json'),
            data=data,
            params={'api-version': 'v2'}
        )

    def put(self, resourceID, data=None):
        return self.manager.put(
            self.manager.buildURI('/resources/{}.json'.format(resourceID)),
            data=data
        )

    def delete(self, resourceID):
        return self.manager.delete(
            self.manager.buildURI('/resources/{}.json'.format(resourceID))
        )
