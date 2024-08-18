import string
import random

def get_user_preferences():
    while True:
        try:
            length = int(input("Enter the desired password length (must be greater than 10): "))
            if length <= 10:
                print("Password length must be greater than 10. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print("Select the character types you want to include in your password:")
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_punctuation = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Ensure at least one character type is selected
    if not (include_lowercase or include_uppercase or include_digits or include_punctuation):
        print("You must select at least one character type. Please start again.")
        return get_user_preferences()

    return length, include_lowercase, include_uppercase, include_digits, include_punctuation

def generate_password(length, include_lowercase, include_uppercase, include_digits, include_punctuation):
    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation

    # Ensure the password contains at least one of each selected character type
    password = []
    if include_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_digits:
        password.append(random.choice(string.digits))
    if include_punctuation:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random characters from the selected types
    password += random.choices(characters, k=length - len(password))

    # Shuffle the result to avoid predictable patterns
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

def display_password(password):
    print(f"Generated Password: {password}")

def main():
    print("Random Password Generator")
    length, include_lowercase, include_uppercase, include_digits, include_punctuation = get_user_preferences()
    password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_punctuation)
    display_password(password)

if __name__ == "__main__":
    main()
