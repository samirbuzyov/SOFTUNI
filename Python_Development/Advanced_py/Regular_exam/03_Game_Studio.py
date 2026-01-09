def sort_games(*games : tuple[str, str], **release_ids):
    console_games = {}
    pc_games = {}
    for game in games:
        if game[0] == 'pc':
            for key, value in release_ids.items():
                if game[1] == value:
                    pc_games[key] = game[1]
        elif game[0] == 'console':
            for key, value in release_ids.items():
                if game[1] == value:
                    console_games[key] = game[1]

    sorted_console = sorted(console_games.items(), key=lambda x: x[0])
    sorted_pc = sorted(pc_games.items(), key=lambda x: x[0], reverse= True)

    result = ''
    if console_games:
        result +="Console Games:\n"
        for k, v in sorted_console:
            result += f">>>{k[:-4]}: {v}\n"
    if pc_games:
        result += "PC Games:\n"
        for k,v in sorted_pc:
            result += f"<<<{k[:-4]}: {v}\n"
    return result
print(sort_games(
    ("pc", "Iron Comet"),
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("pc", "Neon Skyline"),
    ("console", "Blade Echo"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))
print(sort_games(
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("console", "Blade Echo"),
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
))

print(sort_games(
    ("pc", "Iron Comet"),
    ("pc", "Neon Skyline"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))
print(sort_games(
    ("console", "Echo Dive"),
    ("pc", "Quantum Drift"),
    June_22_2025_001="Quantum Drift",
    March_15_2025_002="Echo Dive",
))
