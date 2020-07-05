def is_palindrome(str):
    rev_str = str[::-1]
    if str == rev_str:
        return f'{str} is PALINDROME'
    return f'{str} is NOT PALINDROME'
getString = input("Enter any string to check palindrome \n")
print(is_palindrome(getString))