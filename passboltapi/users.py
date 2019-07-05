from .meta import PassboltAPIEndpoint


class PassboltUsersAPI(PassboltAPIEndpoint):
    def get(self, userID=None, params={}):
        if userID:
            return self.manager.get(
                self.manager.buildURI('/users/{}.json'.format(userID))
            )
        else:
            return self.manager.get(
                self.manager.buildURI('/users.json'),
                params=params
            )

    def post(self, data=None):
        return self.manager.post(
            self.manager.buildURI('/users.json'),
            data=data
        )

    def put(self, userID, data=None):
        return self.manager.put(
            self.manager.buildURI('/users/{}.json'.format(userID)),
            data=data
        )

    def delete(self, userID, dryRun=False):
        if dryRun:
            return self.manager.delete(
                self.manager.buildURI('/users/{}/dry-run'.format(userID))
            )
        else:
            return self.manager.delete(
                self.manager.buildURI('/users/{}.json'.format(userID))
            )
