class StringReverser:
    def __init__(self, text):
        self._text = text  # Encapsulated attribute
    
    def reverse_words(self):
        """Reverse the string word by word"""
        words = self._text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
    
    def reverse_characters(self):
        """Reverse the entire string character by character"""
        return self._text[::-1]
    
    def reverse_each_word(self):
        """Reverse each word individually but maintain word order"""
        words = self._text.split()
        reversed_each = [word[::-1] for word in words]
        return ' '.join(reversed_each)
    
    def get_original(self):
        """Getter for original text"""
        return self._text
    
    def set_text(self, new_text):
        """Setter for text with validation"""
        if isinstance(new_text, str):
            self._text = new_text
        else:
            raise ValueError("Input must be a string")
    
    def __str__(self):
        """Special method: string representation"""
        return f"StringReverser: '{self._text}'"
    
    def __repr__(self):
        """Special method: detailed representation"""
        return f"StringReverser('{self._text}')"
    
    def __len__(self):
        """Special method: length of the string"""
        return len(self._text)
    
    def __add__(self, other):
        """Special method: concatenation"""
        if isinstance(other, StringReverser):
            return StringReverser(self._text + other._text)
        elif isinstance(other, str):
            return StringReverser(self._text + other)
        else:
            raise TypeError("Can only concatenate with StringReverser or str")

# Example usage
def main():
    # Create StringReverser object
    original_text = "Hello World from Python Programming"
    reverser = StringReverser(original_text)
    
    print("Original Text:", reverser.get_original())
    print("String representation:", reverser)
    print("Length of string:", len(reverser))
    print()
    
    # Different reversal methods
    print("1. Reverse words order:", reverser.reverse_words())
    print("2. Reverse characters:", reverser.reverse_characters())
    print("3. Reverse each word:", reverser.reverse_each_word())
    print()
    
    # Demonstration of special methods
    reverser2 = StringReverser(" Another String")
    combined = reverser + reverser2
    print("Combined strings:", combined.get_original())
    print("Combined reverse words:", combined.reverse_words())

if __name__ == "__main__":
    main()
