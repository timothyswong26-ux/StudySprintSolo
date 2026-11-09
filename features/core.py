"""Core StudySprint logic: the deck, the quiz loop, and small helpers."""


def get_cards(data):
    return data["cards"]


def check_answer(card, guess):
    return guess.strip().lower() == card["answer"].strip().lower()


def run_quiz(cards, ask=input, show=print):
    score = 0
    for card in cards:
        guess = ask(card["question"] + " ")
        if check_answer(card, guess):
            show("Correct!")
            score += 1
        else:
            show("Not quite. The answer was: " + card["answer"])
    return score


def add_card(data, question, answer, category="general"):
    new_id = max((c["id"] for c in data["cards"]), default=0) + 1
    card = {"id": new_id, "question": question, "answer": answer, "category": category}
    data["cards"].append(card)
    return card


def list_cards(cards, show=print):
    for card in cards:
        show(str(card["id"]) + ". " + card["question"])


def cards_by_category(cards, category):
    return [c for c in cards if c["category"] == category]


def count_by_category(cards):
    counts = {}
    for card in cards:
        name = card["category"]
        counts[name] = counts.get(name, 0) + 1
    return counts


def top_card(cards):
    return cards[len(cards) - 1]


def percent_correct(score, total):
    if total == 0:
        return 0
    return round(100 * score / total)

def review_missed(cards, results):
    return [card for card, is_correct in zip(cards, results) if not is_correct]

def best_streak(results):
    max_streak = 0
    current_streak = 0
    for r in results:
        if r:
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            current_streak = 0
    return max_streak


import csv

def import_cards_from_csv(file_path, start_id=1):
    cards = []
    current_id = start_id
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            card = dict(row)
            card['id'] = current_id
            cards.append(card)
            current_id += 1
    return cards


import time

def run_lightning_round(cards):
    if not cards:
        print("No cards available for the lightning round!")
        return 0, 0.0

    score = 0
    start_time = time.time()
    
    for card in cards:
        print(f"\nQuestion: {card.get('question')}")
        user_answer = input("Your answer: ").strip()
        
        correct_answer = card.get('answer')
        if user_answer.lower() == str(correct_answer).lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}")
            
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    
    print(f"\n--- Lightning Round Complete ---")
    print(f"Score: {score}/{len(cards)}")
    print(f"Time Taken: {elapsed_time} seconds")
    
    return score, elapsed_time
import random

def generate_multiple_choice(card, deck):
    
    correct_answer = card.get('answer')
    
    wrong_answers = []
    seen = {correct_answer}
    
    for c in deck:
        ans = c.get('answer')
        if ans not in seen:
            seen.add(ans)
            wrong_answers.append(ans)
            
    num_to_sample = min(3, len(wrong_answers))
    selected_wrong = random.sample(wrong_answers, num_to_sample) if num_to_sample > 0 else []
    
    options = [correct_answer] + selected_wrong
    random.shuffle(options)
    
    return options

def progress_bar(current, total, length=10):
    """Returns a text progress bar string like [###-------] 3/8."""
    if total <= 0:
        filled = 0
    else:
        filled = int(round((current / total) * length))
    
    filled = max(0, min(filled, length))
    empty = length - filled
    bar = "#" * filled + "-" * empty
    return f"[{bar}] {current}/{total}"
def run_quiz(cards):
    """Runs the normal quiz loop and prints a progress bar before each question."""
    score = 0
    total = len(cards)
    
    for i, card in enumerate(cards, start=1):
        # Print progress bar before each question (e.g., [###-------] 3/8)
        print(f"\n{progress_bar(i - 1, total)}")
        print(f"Question: {card.get('question')}")
        
        answer = input("Your answer: ").strip()
        correct = str(card.get('answer')).strip()
        
        if answer.lower() == correct.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {correct}")
            
    # Show final progress bar at completion
    print(f"\n{progress_bar(total, total)}")
    return score