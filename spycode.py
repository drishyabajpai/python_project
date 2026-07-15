import random
import string

def random_letters():
    return ''.join(random.choices(string.ascii_letters,  k=3))


while True:
    print("\n===SECRET CODE===")
    print("1. Generate a random code")
    print("2. Decrypt a code")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
         message = input("\n Enter your message: ")
         words = message .split()
         encoded_message = []

         for word in words:
              if len(word) >= 3:
                    first_letter = word[0]
                    new_word = word[1:] + first_letter
                    new_word = random_letters() + new_word + random_letters()
                    encoded_message.append(new_word)

              else:
                    encoded_message.append(word[::-1])

         print(f"Encoded message: {' '.join(encoded_message)}")
         print("Your message has been encoded successfully!")

    elif choice == '2':
        message = input("\nEnter the secret code: ")
        words = message.split()
        decoded_message = []

        for word in words:
            if len(word) >= 3:
                word = word[3:-3]
                first_letter = word[-1]
                new_word = first_letter + word[:-1]
                decoded_message.append(new_word)
            else:
                decoded_message.append(word[::-1])

        print(f"Decoded message: {' '.join(decoded_message)}")
        print("Your message has been decoded successfully!")

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")