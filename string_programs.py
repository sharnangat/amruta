"""
String Programs in Python

A beginner-friendly menu program for string logic practice.
"""


def reverse_string(text):
    return text[::-1]


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def count_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count


def character_frequency(text):
    freq = {}
    for ch in text:
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1
    return freq


def remove_spaces(text):
    return text.replace(" ", "")


def word_count(text):
    words = text.strip().split()
    return len(words)


def are_anagrams(first, second):
    s1 = sorted(ch.lower() for ch in first if ch.isalnum())
    s2 = sorted(ch.lower() for ch in second if ch.isalnum())
    return s1 == s2


def find_longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)


def show_menu():
    print("\n=== String Programs Menu ===")
    print("1. Reverse String")
    print("2. Palindrome Check")
    print("3. Count Vowels and Consonants")
    print("4. Character Frequency")
    print("5. Remove Spaces")
    print("6. Word Count")
    print("7. Anagram Check")
    print("8. Longest Word in Sentence")
    print("9. Exit")


def main():
    print("String Practice Program")

    while True:
        show_menu()
        choice = input("Enter choice (1-9): ").strip()

        if choice == "9":
            print("Goodbye!")
            break

        if choice == "1":
            text = input("Enter a string: ")
            print(f"Reversed: {reverse_string(text)}")

        elif choice == "2":
            text = input("Enter a string: ")
            if is_palindrome(text):
                print("It is a palindrome.")
            else:
                print("It is not a palindrome.")

        elif choice == "3":
            text = input("Enter a string: ")
            vowels, consonants = count_vowels_and_consonants(text)
            print(f"Vowels: {vowels}, Consonants: {consonants}")

        elif choice == "4":
            text = input("Enter a string: ")
            freq = character_frequency(text)
            if not freq:
                print("No characters to count.")
            else:
                print("Character frequency:")
                for ch in sorted(freq):
                    print(f"{ch} -> {freq[ch]}")

        elif choice == "5":
            text = input("Enter a string: ")
            print(f"Without spaces: {remove_spaces(text)}")

        elif choice == "6":
            text = input("Enter a sentence: ")
            print(f"Word count: {word_count(text)}")

        elif choice == "7":
            first = input("Enter first string: ")
            second = input("Enter second string: ")
            if are_anagrams(first, second):
                print("Strings are anagrams.")
            else:
                print("Strings are not anagrams.")

        elif choice == "8":
            text = input("Enter a sentence: ")
            longest = find_longest_word(text)
            if longest:
                print(f"Longest word: {longest}")
            else:
                print("No words found.")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
