"""StudySprint - a small flashcard and quiz trainer.

Run it with:  python main.py
"""

import storage
from features import core, reports
from features.core import import_cards_from_csv

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
    print("8) Import csv")
    print("9) Quit")
    print("10) Lightning round")
    


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
            print("You scored " + str(score) + "/" + str(total) +
                  " (" + str(core.percent_correct(score, total)) + "%).")
            if "history" not in data:
                data["history"] = []
                data["history"].append(score) # or a dict like {"score": score, "total": total}
                storage.save_data(data)
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
        elif choice == "8":
            file_path = input("Enter path to CSV file: ").strip()
            
            cards_list = data["cards"] if isinstance(data, dict) and "cards" in data else data
            start_id = len(cards_list) + 1
            
            try:
                new_cards = import_cards_from_csv(file_path, start_id=start_id)
                
                if isinstance(data, dict) and "cards" in data:
                    data["cards"].extend(new_cards)
                elif isinstance(data, list):
                    data.extend(new_cards)
                    
                storage.save_data(data)
                print(f"Successfully imported and saved {len(new_cards)} cards!")
            except (FileNotFoundError, OSError):
                print(f"Error: Could not find or open file at '{file_path}'. Please check the path and try again.")
        elif choice == "9":
            print("Goodbye!")
            break
        elif choice == "10":
            from features.core import run_lightning_round
            cards_list = data["cards"] if isinstance(data, dict) and "cards" in data else data
            run_lightning_round(cards_list)
        elif choice == "11":
            if not cards:
                cards = core.get_cards(data)
            if not cards:
                print("No cards available! Add some cards or import from CSV first.")
                continue
            
            print("\n--- Multiple-Choice Quiz ---")
            score = 0
            for card in cards:
                print(f"\nQuestion: {card.get('question')}")
                options = core.generate_multiple_choice(card, cards)
                
                for i, opt in enumerate(options, 1):
                    print(f"  {i}. {opt}")
                    
                choice_idx = input("Choose option number: ").strip()
                try:
                    idx = int(choice_idx) - 1
                    if 0 <= idx < len(options) and options[idx] == card.get('answer'):
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Incorrect. Correct answer was: {card.get('answer')}")
                except ValueError:
                    print(f"Invalid input. Correct answer was: {card.get('answer')}")
                    
            print(f"\nMultiple-Choice Quiz Complete! Score: {score}/{len(cards)}") 
        elif choice == "12":
            history = data.get("history", [])
            if not history:
                print("\nNo quiz history recorded yet.")
            else:
                print("\n=== Recent Quiz Scores == (Last 5) ===")
                # Show the last few scores (e.g., last 5)
                recent = history[-5:]
                for i, s in enumerate(recent, 1):
                    print(f"{i}. Score: {s}")           
        else:
            print("Please pick a number from the menu.")
        


if __name__ == "__main__":
    main()
