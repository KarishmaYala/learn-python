
def is_palindrome(value):
    #processing special chars and spaces to consider only normal chars for Palindrome.
    value = ''.join(value.split())
    value = value.replace('.', '')
    value = value.lower()
    return value == value[::-1]

print(is_palindrome(input('Enter the value: ')),
      is_palindrome(input('Enter the value: ')),
      is_palindrome(input('Enter the value: ')),
      is_palindrome(input('Enter the value: ')))
