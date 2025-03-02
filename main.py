from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """
    Simulates an attack by a character and returns the damage dealt.

    Keyword arguments:
    char_name (str): The name of the character performing the attack.
    char_class (str): The class of the character, which determines the
    damage range.
    Possible values are "warrior", "mage", and "healer".
    """
    char_class = ""

    if char_class == "warrior":
        return f"{char_name} нанёс урон противнику равный {5 + randint(3, 5)}"
    if char_class == "mage":
        return f"{char_name} нанёс урон противнику равный {5 + randint(5, 10)}"
    if char_class == "healer":
        damage = 5 + randint(-3, -1)
        return f"{char_name} нанёс урон противнику равный {damage}"
    return char_class


def defence(char_name: str, char_class: str) -> str:
    """
    Calculate the amount of damage blocked by a character based on their class.

    Keyword arguments:
        char_name (str): The name of the character.
        char_class (str): The class of the character, which can be "warrior",
        "mage", or "healer".
    """
    char_class = ""

    if char_class == "warrior":
        return f"{char_name} блокировал {10 + randint(5, 10)} урона"
    if char_class == "mage":
        return f"{char_name} блокировал {10 + randint(-2, 2)} урона"
    if char_class == "healer":
        return f"{char_name} блокировал {10 + randint(2, 5)} урона"
    return char_class


def special(char_name: str, char_class: str) -> str:
    """
    Apply a special ability based on the character's class.

    Keyword arguments:
    char_name (str): The name of the character.
    char_class (str): The class of the character, which can be "warrior",
    "mage", or "healer".
    """
    char_class = ""

    if char_class == "warrior":
        return (
            f"{char_name} применил специальное умение "
            "«Выносливость {80 + 25}»"
        )
    if char_class == "mage":
        return f"{char_name} применил специальное умение «Атака {5 + 40}»"
    if char_class == "healer":
        return f"{char_name} применил специальное умение «Защита {10 + 30}»"
    return ""


def start_training(char_name: str, char_class: str) -> str:
    """
    Initiates training for a character based on their class.

    Keyword arguments:
    char_name (str): The name of the character.
    char_class (str): The class of the character. Can be "warrior",
                      "mage", or "healer".
    """

    if char_class == "warrior":
        print(f"{char_name}, ты Воитель — отличный боец ближнего боя.")
    if char_class == "mage":
        print(f"{char_name}, ты Маг — превосходный укротитель стихий.")
    if char_class == "healer":
        print(f"{char_name}, ты Лекарь — чародей, способный исцелять раны.")
    print("Потренируйся управлять своими навыками.")
    print("Введи одну из команд: attack — чтобы атаковать противника, ")
    print("defence — чтобы блокировать атаку противника или")
    print("special — чтобы использовать специальное умение.")
    print("Если не хочешь тренироваться, введи команду skip.")
    cmd = ""
    while cmd != "skip":
        cmd = input("Введи команду: ")
        if cmd == "attack":
            print(attack(char_name, char_class))
        if cmd == "defence":
            print(defence(char_name, char_class))
        if cmd == "special":
            print(special(char_name, char_class))
    return "Тренировка окончена."


def choice_char_class() -> str:
    """
    Prompt the user to choose a character class and confirm the choice.
    The function repeatedly asks the user to input a character class
    (warrior, mage, or healer) and provides a description of the chosen class.
    The user must confirm their choice by pressing 'y'. If the user presses
    any other key, they are prompted to choose again.
    """
    approve_choice: str = ""
    char_class: str = ""
    while approve_choice != "y":
        char_class = input(
            "Введи название персонажа, "
            "за которого хочешь играть: Воитель — warrior, "
            "Маг — mage, Лекарь — healer: "
        )
        if char_class == "warrior":
            print(
                "Воитель — дерзкий воин ближнего боя. "
                "Сильный, выносливый и отважный."
            )
        if char_class == "mage":
            print(
                "Маг — находчивый воин дальнего боя. "
                "Обладает высоким интеллектом."
            )
        if char_class == "healer":
            print(
                "Лекарь — могущественный заклинатель. "
                "Черпает силы из природы, веры и духов."
            )
        approve_choice = input(
            "Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, "
            "чтобы выбрать другого персонажа "
        ).lower()
    return char_class


def main() -> None:
    print("Приветствую тебя, искатель приключений!")
    print("Прежде чем начать игру...")
    char_name: str = input("...назови себя: ")
    print(
        f"Здравствуй, {char_name}! "
        "Сейчас твоя выносливость — 80, атака — 5 и защита — 10."
    )
    print("Ты можешь выбрать один из трёх путей силы:")
    print("Воитель, Маг, Лекарь")
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


main()

if __name__ == "__main__":
    run_screensaver()
    print("Приветствую тебя, искатель приключений!")
    print("Прежде чем начать игру...")
    char_name: str = input("...назови себя: ")
    print(
        f"Здравствуй, {char_name}! "
        "Сейчас твоя выносливость — 80, атака — 5 и защита — 10."
    )
    print("Ты можешь выбрать один из трёх путей силы:")
    print("Воитель, Маг, Лекарь")
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
