from .meta import PassboltAPIEndpoint


class PassboltGroupsAPI(PassboltAPIEndpoint):
    def get(self, groupID=None, params={}):
        if groupID:
            return self.manager.get(
                self.manager.buildURI('/groups/{}.json'.format(groupID))
            )
        else:
            return self.manager.get(
                self.manager.buildURI('/groups.json'),
                params=params
            )

    def post(self, data):
        return self.manager.post(
            self.manager.buildURI('/groups.json'),
            data=data
        )

    def put(self, groupID, data, dryRun=False):
        if dryRun:
            return self.manager.put(
                self.manager.buildURI('/groups/{}/dry-run'.format(groupID)),
                data=data
            )
        else:
            return self.manager.put(
                self.manager.buildURI('/groups/{}.json'.format(groupID)),
                data=data
            )

    def delete(self, groupID, dryRun=False):
        if dryRun:
            return self.manager.delete(
                self.manager.buildURI('/groups/{}/dry-run'.format(groupID))
            )
        else:
            return self.manager.delete(
                self.manager.buildURI('/groups/{}.json'.format(groupID))
            )
