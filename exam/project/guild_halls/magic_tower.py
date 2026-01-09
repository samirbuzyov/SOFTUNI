from project.guild_halls.base_guild_hall import BaseGuildHall


class MagicTower(BaseGuildHall):
    MAX_MEMBERS = 4

    def __init__(self, alias):
        super().__init__(alias)

    @property
    def max_member_count(self) -> int:
        return self.MAX_MEMBERS

    def increase_gold(self,min_skill_level_value: int):
        for member in self.members:
            if member.skill_level >= min_skill_level_value and member.role == 'Mage':
                member.gold *= 2
