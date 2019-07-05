from passboltapi.meta import PassboltAPIEndpoint


class PassboltAuthAPI(PassboltAPIEndpoint):
    def get(self):
        return self.manager.get(self.manager.buildURI('/auth/verify.json'))
