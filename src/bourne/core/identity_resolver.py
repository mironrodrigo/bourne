from bourne.db.models.profile import Profile
from bourne.db.models.resolution_rule import ResolutionRule

class IdentityResolver:
    def __init__(self, profile_repo, rule_repo):
        self.profile_repo = profile_repo
        self.rule_repo = rule_repo

    async def resolve(self, tenant_id: str, identifiers: dict) -> str:
        rules = await self.rule_repo.get(tenant_id)

        # ToDo continue...
