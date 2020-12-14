def is_palindrome(text):
    left = 0
    right = len(text)-1
    while True:
        if right < left:
            return True
        if text[left].lower() == text[right].lower():
            left += 1
            right -= 1
        else:
            return False


print("jumla", "is a palindrome", is_palindrome("jumla"))
print("txt", "is a palindrome", is_palindrome("txt"))
print("civic", "is a palindrome", is_palindrome("civic"))
print("radar", "is a palindrome", is_palindrome("radar"))
print("goku", "is a palindrome", is_palindrome("goku"))