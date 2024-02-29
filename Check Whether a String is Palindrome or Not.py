def is_palindrome(s):
    # Removing spaces and converting to lowercase for case-insensitive comparison
    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string: ")

    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
