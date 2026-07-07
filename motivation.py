import random

quotes = [
    {
        "quote": "Stay hungry, stay foolish.",
        "author": "Steve Jobs"
    },
    {
        "quote": "The best way to predict the future is to invent it.",
        "author": "Alan Kay"
    },
    {
        "quote": "First, solve the problem. Then, write the code.",
        "author": "John Johnson"
    },
    {
        "quote": "Code is like humor. When you have to explain it, it's bad.",
        "author": "Cory House"
    },
    {
        "quote": "Success is the sum of small efforts repeated day in and day out.",
        "author": "Robert Collier"
    },
    {
        "quote": "Discipline is choosing between what you want now and what you want most.",
        "author": "Abraham Lincoln"
    }
]


def show_quote():
    quote = random.choice(quotes)

    print("\n" + "=" * 50)
    print("                RANdOM QUOTE GENERATOR")
    print("=" * 50)
    print(f"\n\"{quote['quote']}\"") #explaining the use of f-string to format the quote and author
    print(f" - {quote['author']}\n") # the explanation of the f-string is that it allows for the inclusion of variables and expressions inside a string by using curly braces {}. In this case, the quote and author are being inserted into the string using f-strings.
    print("=" * 50 )


while True:
    show_quote()
    user_input = input("Press Enter to see another quote or type 'exit' to quit: ")
    if user_input.lower() == 'exit':
        break 
    