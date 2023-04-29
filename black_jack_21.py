import random


def deal_card():
    """Возвращает случайную карту из колоды."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Возвращает сумму очков на руках."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Сравнивает результаты игры."""
    if user_score == computer_score:
        return "Ничья!"
    elif computer_score == 0:
        return "Вы проиграли, у компьютера блэкджек!"
    elif user_score == 0:
        return "Вы выиграли, у вас блэкджек!"
    elif user_score > 21:
        return "Вы проиграли, у вас перебор!"
    elif computer_score > 21:
        return "Вы выиграли, у компьютера перебор!"
    elif user_score > computer_score:
        return "Вы выиграли!"
    else:
        return "Вы проиграли!"


def play_game():
    """Основная функция игры."""
    print("Добро пожаловать в игру Блэкджек!")

    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(
            f"Ваши карты: {user_cards}, текущий счёт: {user_score}")
        print(f"Карта компьютера: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_card = input(
                "Хотите взять еще карту? Введите 'y' или 'n': ").lower()
            if draw_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(
        f"Ваши карты: {user_cards}, текущий счёт: {user_score}")
    print(
        f"Карты компьютера: {computer_cards}, текущий счёт: {computer_score}")
    print(compare(user_score, computer_score))


while input("Хотите сыграть в игру Блэкджек? Введите 'y' или 'n': ").lower() == "y":
    play_game()
