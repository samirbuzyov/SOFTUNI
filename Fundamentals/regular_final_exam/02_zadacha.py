import re


def surrounded_by(text: str) -> bool:
    if ":" not in text:
        return False
    first_word, second_word = text.split(':')
    pattern = r'![A-Z][a-z]*!'
    return bool(re.fullmatch(pattern, first_word))


def check_len(text: str) -> bool:
    if ":" not in text:
        return False
    first_word, second_word = text.split(':', 1)
    return len(first_word) >= 3


def check_colon(text: str) -> bool:
    return text.count(':') == 1


def consist_alphaletters(text: str) -> bool:
    if ":" not in text:
        return False
    first_word, second_word = text.split(':', 1)
    pattern = r'\[([A-Za-z]+)\]'
    return bool(re.search(pattern, second_word))


def min_eight(text: str) -> bool:
    return len(text) > 8


n = int(input())

for _ in range(n):
    command = input()

    if (surrounded_by(command) and consist_alphaletters(command) and
            min_eight(command) and check_colon(command) and check_len(command)):

        first_word, second_word = command.split(':')

        command_match = re.search(r'!([A-Z][a-z]*)!', first_word)
        command_text = command_match.group(1) if command_match else "Unknown"

        match = re.search(r'\[([A-Za-z]+)\]', second_word)
        if match:
            word = match.group(1)
            ascii_values = [str(ord(char)) for char in word]
            print(f"{command_text}: {' '.join(ascii_values)}")
        else:
            print("The message is invalid")

    else:
        print("The message is invalid")
