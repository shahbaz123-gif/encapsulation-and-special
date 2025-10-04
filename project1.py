def reverse_words_comprehension(s):
    """
    Reverse a string word by word using list comprehension
    """
    words = s.split()
    reversed_string = ' '.join([words[i] for i in range(len(words)-1, -1, -1)])
    return reversed_string

# Test
text = "Learn Python programming"
result = reverse_words_comprehension(text)
print(f"Original: '{text}'")
print(f"Reversed: '{result}'")