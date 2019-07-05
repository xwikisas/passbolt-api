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

    def post(self, data=None):
        return self.manager.post(
            self.manager.buildURI('/resources.json'),
            data=data
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
