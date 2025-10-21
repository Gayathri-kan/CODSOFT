import random
import string

def generate_password(length):
    # Combine all possible characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters for the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Ask the user for password length
try:
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Password length should be at least 4 for better security.")
    else:
        # Generate and display password
        new_password = generate_password(length)
        print("\nGenerated Password:", new_password)
except ValueError:
    print("Please enter a valid number.")
