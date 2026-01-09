from project.guild_halls.base_guild_hall import BaseGuildHall
from project.guild_halls.combat_hall import CombatHall
from project.guild_halls.magic_tower import MagicTower
from project.guild_members.base_guild_member import BaseGuildMember
from project.guild_members.mage import Mage
from project.guild_members.warrior import Warrior


class GuildMaster:
    def __init__(self):
        self.members:list[BaseGuildMember] = []
        self.guild_halls : list[BaseGuildHall] = []

    def add_member(self, member_type: str, member_tag: str, member_gold: int):
        valid_types = ["Warrior", "Mage"]
        if member_type not in valid_types:
            raise ValueError("Invalid member type!")
        for member in self.members:
            if member.tag == member_tag:
                raise ValueError(f"{member_tag} has already been added!")
        new_member = None
        if member_type == 'Warrior':
            new_member = Warrior(member_tag, member_gold)
        elif member_type == 'Mage':
            new_member = Mage(member_tag, member_gold)

        self.members.append(new_member)
        return f"{member_tag} is successfully added as {member_type}."

    def add_guild_hall(self, guild_hall_type: str, guild_hall_alias: str):
        valid_types = ["CombatHall", "MagicTower"]
        if not guild_hall_type in valid_types:
            raise ValueError("Invalid guild hall type!")

        for hall in self.guild_halls:
            if guild_hall_alias == hall.alias:
                raise ValueError(f"{guild_hall_alias} has already been added!")
        new_hall = None
        if guild_hall_type == 'CombatHall':
            new_hall = CombatHall(guild_hall_alias)
        elif guild_hall_type == 'MagicTower':
            new_hall = MagicTower(guild_hall_alias)

        self.guild_halls.append(new_hall)
        return f"{guild_hall_alias} is successfully added as a {guild_hall_type}."

    def assign_member(self, guild_hall_alias: str, member_type: str):
        hall = next((h for h in self.guild_halls if h.alias == guild_hall_alias), None)
        if hall is None:
            raise ValueError(f"Guild hall {guild_hall_alias} does not exist!")

        if member_type == "Warrior":
            member = next((m for m in self.members if isinstance(m, Warrior)), None)
        elif member_type == "Mage":
            member = next((m for m in self.members if isinstance(m, Mage)), None)
        else:
            raise ValueError("Invalid member type!")

        if member is None:
            raise ValueError("No available members of the type!")

        if len(hall.members) >= hall.max_member_count:
            return "Maximum member count reached. Assignment is impossible."

        self.members.remove(member)
        hall.members.append(member)
        return f"{member.tag} was assigned to {guild_hall_alias}."

    def practice_members(self, guild_hall: BaseGuildHall, sessions_number: int):
        for _ in range(sessions_number):
            for member in guild_hall.members:
                member.practice()

        total_skill_level = sum(member.skill_level for member in guild_hall.members)

        return f"{guild_hall.alias} members have {total_skill_level} total skill level after {sessions_number} practice session/s."

    def unassign_member(self, guild_hall: BaseGuildHall, member_tag: str):
        member = next((member for member in guild_hall.members if member.tag == member_tag), None)
        if member is None or member.skill_level == 10:
            return "The unassignment process was canceled."

        guild_hall.members.remove(member)
        self.members.append(member)
        return f"Unassigned member {member_tag}."

    def guild_update(self, min_skill_level_value: int):
        for hall in self.guild_halls:
            hall.increase_gold(min_skill_level_value)

        sorted_halls = sorted(
            self.guild_halls,
            key=lambda h: (-len(h.members), h.alias)
        )
        result = ["<<<Guild Updated Status>>>", f"Unassigned members count: {len(self.members)}",
                  f"Guild halls count: {len(self.guild_halls)}"]
        for hall in sorted_halls:
            result.append(f">>>{hall.status()}")

        return "\n".join(result)

