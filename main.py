from random import randint


def user_interfaca(options):
    """"
    Дает пользователю выбор из нескольких вариантов
   """
    for index, weapon in enumerate(options):
        print(f'{index} = {weapon}')
    try:
        user_input = int(input('what do you choose? '))
        return user_input
    except ValueError:
        print(f'Please, use numbers!'), main()


def computer_choice(content):
    comp_choise = randint(0, len(content) - 1)
    return comp_choise


def check_result(choises, player, copm):
    if player == copm:
        print("It's a tie!")
    elif (player == 0 and copm == len(choises) - 1) or (
            player > copm and not (player == len(choises) - 1 and copm == 0)):
        return "Player Won!"
    return 'Wasted'


def play():
    print("==========================\n"
          "Welcome to my game!\n"
          "Please, pick your weapon\n"
          "==========================")

    # объявили список возможных варианто для выбора
    option_list = ('Rock', 'Paper', 'Scissors')
    user_result = user_interfaca(option_list)
    coputer_result = computer_choice(option_list)

    # показываем выбор игрока
    try:
        print(f'plaeys choose: {option_list[user_result]}')
        print(f'computer choose: {option_list[coputer_result]}')

        result = check_result(option_list, user_result, coputer_result)
        print(f'\n{result}')
    except (IndexError, TypeError):
        print(f'Please, try again you are out of line')
        play()


def main():
    flag = ''
    while flag.lower() != 'n':
        play()
        print('Do you to try again?')
        flag = input('Y to continue or N to stop the game: ')


main()
