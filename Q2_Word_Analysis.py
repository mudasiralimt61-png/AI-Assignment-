sentence = input("Enter a sentence: ")

words = sentence.split()
characters = len(sentence)

if len(words) == 0:
    print("Please enter a sentence with words.")
else:
    longest = words[0]
    shortest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word
        if len(word) < len(shortest):
            shortest = word

    vowels = 0
    for character in sentence.lower():
        if character in "aeiou":
            vowels += 1

    unique_words = set(words)
    alphabetical_words = sorted(words, key=str.lower)

    print("Total words:", len(words))
    print("Total characters:", characters)
    print("Longest word:", longest)
    print("Shortest word:", shortest)
    print("Vowel count:", vowels)
    print("Unique words:", unique_words)
    print("Alphabetical order:", alphabetical_words)

    with open("word_analysis.txt", "w", encoding="utf-8") as file:
        file.write("Sentence: " + sentence + "\n")
        file.write("Total words: " + str(len(words)) + "\n")
        file.write("Total characters: " + str(characters) + "\n")
        file.write("Longest word: " + longest + "\n")
        file.write("Shortest word: " + shortest + "\n")
        file.write("Vowel count: " + str(vowels) + "\n")
        file.write("Unique words: " + str(unique_words) + "\n")
        file.write("Alphabetical order: " + str(alphabetical_words) + "\n")

    print("Analysis saved in word_analysis.txt")
