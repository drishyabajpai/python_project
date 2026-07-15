import random
import string

# Generate random letters
def random_letters():
    return ''.join(random.choices(string.ascii_letters, k=3))


while True:

    print("\n====== SECRET CODE LANGUAGE ======")
    print("1. Encode Message")
    print("2. Decode Message")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # ------------------ ENCODE ------------------
    if choice == "1":

        message = input("\nEnter your message: ")

        words = message.split()

        encoded_message = []

        for word in words:

            if len(word) >= 3:

                first_letter = word[0]

                new_word = word[1:] + first_letter

                new_word = random_letters() + new_word + random_letters()

                encoded_message.append(new_word)

            else:

                encoded_message.append(word[::-1])

        print("\nEncoded Message:")
        print(" ".join(encoded_message))


    # ------------------ DECODE ------------------
    elif choice == "2":

        message = input("\nEnter secret code: ")

        words = message.split()

        decoded_message = []

        for word in words:

            if len(word) >= 3:

                word = word[3:-3]

                original = word[-1] + word[:-1]

                decoded_message.append(original)

            else:

                decoded_message.append(word[::-1])

        print("\nDecoded Message:")
        print(" ".join(decoded_message))


    # ------------------ EXIT ------------------
    elif choice == "3":

        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!")