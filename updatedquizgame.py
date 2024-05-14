# def for new functions, tables, etc.

# adding variables (to define)

questions = (
    "What is Python?: ", # 1
    "What's new in Python 3.12.2?: ", # 2
    "Why Python?: ", # 3
    "How to install Python?: ", # 4
    "Why is it called Python?: ", # 5
    "How do you submit bug reports and patches for Python?: ", # 6
    "How stable is Python?: ", # 7
    "Are there any books on Python?: ", # 8
    "How many people are using Python?: ", # 9
    "Are there copyright restrictions on the use of Python?: " # 10
)

options = (
    ("A. interpreted, object-oriented programming language", "B. interpretted, object-oriented programming language", "C. interpreted, objekt-oriented programming language", "D. compiled, object-oriented programming language"),
    ("A. the distutil package has been removed from the standard library", "B. the distutils pakcage has been removed from the standard library", "C. the distutils package has been removed from the library", "D. the distutils package has been removed from the standard library"),
    ("A. simple syntacs, easy to understand and learn", "B. simple syntax, easy to understand and learn", "C. simple syntax, easy to not understand, but learn", "D. simple syntax, easy to understand, but not learn"),
    ("A. https://www.python.com/downloads/", "B. https://www.python.co/downloads/", "C. https://www.python.org/downloads/", "D. https://www.python.org/download"),
    ("A. Van Rossum needed a name that was short, unique, and slightly mysterious, so he called it the Python", "B. Van Rossumes needed a name that was short, unique, and slightly mysterious, so he decided to call the language Python", "C. Van Rossum needed a name that was small, unique, and slightly mysterious, so he decided to call the language Python", "D. None"),
    ("A. To report a bug or submit a patch, used issue tracker at: https://github.com/python/cpython/issues.", "B. To report a bug or submit a patch, use the issue tracker at: https://github.com/python/cpython/issues.", "C. To report a bug or submit a patch. Track at: https://github.com/python/cpython/issues.", "D. To report a bug or submit a patch, visit and smash: https://github.com/python/cpython/issues."),
    ("A. Vey Stable", "B. Very Stable", "C. Not stable", "D. None"),
    ("A. Yes, there are many, and more are being published.", "B. Yes, there are many, and more were being published.", "C. Ys, there are many, and more are being published.", "D. No, there aren't."),
    ("A. There are probably millions of users, though it's difficult to obtain an exact count", "B. There are probably millions of users, though it isn't difficult to obtain an exact count", "C. There are probably billions of users, though it's difficult to obtain an exact count", "D. None"),
    ("A. You can do anything you want with the source, as long as you leave the copyrights in and display those copyrights in any documentation about the snake that you produce.", "B. You can do anything you want with it, as long as you leave the copyrights in and display those copyrights in any documentation about Python that you produce.", "C. You can do anything you want with the source, as long as you do not leave the copyrights in and display those copyrights in any documentation about Python that you produce.", "D. You can do anything you want with the source, as long as you leave the copyrights in and display those copyrights in any documentation about Python that you produce.")
)

answers = ("A", "D", "B", "C", "A", "B", "B", "A", "A", "D") # 10 answers


# function to start the quiz
def start():
    # implementing lower for type error handling, and/or friendly typing
    prompt_consent = input("Start? (yes/no)").lower()

    if prompt_consent == "no": # for NO, No, no, or n0 = "no" = all lower case
        print("OK!")
        
    # function to display the questions, if you type "yes". elif (else if)
    elif prompt_consent == "yes":
        play_quiz()

# function to display the questions
def display_question(question, options):
    print(question)
    for option in options:
        print(option)


# function to play the quiz
def play_quiz():
    score = 0
    num_questions = len(questions) # percentage based

    for i in range(num_questions):
        print("\nQuestion {}: ".format(i + 1)) # question order with new line character
        display_question(questions[i], options[i])

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == answers[i]:
            print("Correct!")
            score +=1

        # typed the letter twice, but correct? No problem:
        elif len(user_answer) == 2 and user_answer[0] == answers[i]:
            print("Correct!")
            score += 1

        else:
            print("Incorrect!")

    print("\nQuiz ended!") # nice spacing
    print("Your score: {}/{}".format(score, num_questions)) # from number space number to number/number

start()