from guild_members.base_guild_member import BaseGuildMember


class Mage(BaseGuildMember):
    ROLE = 'Mage'
    SKILL_LEVEL = 1
    def __init__(self, tag:str, gold:int):
        super().__init__(tag,gold,self.ROLE, self.SKILL_LEVEL)

    def practice(self):
        if self.skill_level * 2 <= 10:
            self.skill_level *= 2
        else:
            self.skill_level = 10