"""StudySprint - a small flashcard and quiz trainer.

Run it with:  python main.py
"""

import storage
from features import core, reports


def show_menu():
    print()
    print("=== StudySprint ===")
    print("1) Take the quiz")
    print("2) List cards")
    print("3) Add a card")
    print("4) Study a category")
    print("5) Show the last card")
    print("6) Category breakdown")
    print("7) Deck summary")
    print("0) Quit")


def main():
    data = storage.load_data()
    while True:
        show_menu()
        try:
            choice = input("Pick an option: ").strip()
        except EOFError:
            print()
            break
        if choice == "0":
            print("See you next session!")
            break
        elif choice == "1":
            cards = core.get_cards(data)
            score = core.run_quiz(cards)
            total = len(cards)
            print("You scored " + str(total) + "/" + str(score) +
                  " (" + str(core.percent_correct(score, total)) + "%).")
        elif choice == "2":
            core.list_cards(core.get_cards(data))
        elif choice == "3":
            question = input("Question: ")
            answer = input("Answer: ")
            core.add_card(data, question, answer)
            storage.save_data(data)
            print("Card added.")
        elif choice == "4":
            category = input("Category: ").strip()
            matches = core.cards_by_category(core.get_cards(data), category)
            for card in matches:
                print("- " + card["question"])
        elif choice == "5":
            print(core.top_card(core.get_cards(data))["question"])
        elif choice == "6":
            print(core.count_by_category(core.get_cards(data)))
        elif choice == "7":
            print(reports.deck_summary(data))
        else:
            print("Please pick a number from the menu.")


if __name__ == "__main__":
    main()
