class ProfileRepository:
    def __init__(self, scylla_session):
        self.session = scylla_session

    async def get_by_identifiers(self, identifiers: dict):
        query = "SELECT * FROM profiles HERE identifiers CONTAINS KEY ? AND identifiers[?] = ?"
