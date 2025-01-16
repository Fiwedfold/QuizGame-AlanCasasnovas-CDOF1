import json

def load_questions(filename):
    """
    Load questions from a JSON file.

    Args:
        filename (str): The file to load questions from.

    Returns:
        list: A list of questions.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

def save_questions(filename, questions):
    """
    Save questions to a JSON file.

    Args:
        filename (str): The file to save questions to.
        questions (list): The list of questions to save.
    """
    with open(filename, 'w') as file:
        json.dump(questions, file, indent=4)

def display_menu():
    """
    Display the main menu and return the user's choice.
    """
    print("\nWelcome to the Quiz Game!")
    print("1) Play the quiz")
    print("2) View and add questions")
    print("3) Exit")
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    return choice

def view_and_add_questions(questions, filename):
    """
    View existing questions and allow the user to add new ones.

    Args:
        questions (list): The current list of quiz questions.
        filename (str): The file to save questions to.
    """
    print("\nCurrent Questions:")
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)
        print(f"Answer: {q['answer']}")

    add_new = input("\nDo you want to add a new question? (yes/no): ").strip().lower()
    if add_new in ['yes', 'y']:
        question_text = input("Enter the question text: ").strip()

        num_options = 0
        while num_options not in [2, 3, 4]:
            try:
                num_options = int(input("Enter the number of options (2, 3, or 4): ").strip())
            except ValueError:
                print("Please enter a valid number.")

        options = []
        for i in range(num_options):
            option = input(f"Enter option {chr(65 + i)}: ").strip()
            options.append(f"{chr(65 + i)}) {option}")

        correct_answer = ""
        valid_answers = [chr(65 + i) for i in range(num_options)]
        while correct_answer not in valid_answers:
            correct_answer = input(f"Enter the correct answer ({', '.join(valid_answers)}): ").strip().upper()

        new_question = {
            "question": question_text,
            "options": options,
            "answer": correct_answer
        }
        questions.append(new_question)
        save_questions(filename, questions)
        print("\nNew question added successfully!")

def play_quiz(questions):
    """
    Play the quiz game.

    Args:
        questions (list): The list of quiz questions.
    """
    if not questions:
        print("\nNo questions available! Add some first.")
        return

    print("\nStarting the Quiz!")
    score = 0

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer: ").strip().upper()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nQuiz Over! You scored {score}/{len(questions)}.")

def quiz_game_with_menu():
    """
    Main function to run the quiz game with a menu.
    """
    filename = "questions.json"
    questions = load_questions(filename)

    while True:
        choice = display_menu()

        if choice == '1':
            play_quiz(questions)
        elif choice == '2':
            view_and_add_questions(questions, filename)
        elif choice == '3':
            print("\nThank you for playing! Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")

quiz_game_with_menu()
