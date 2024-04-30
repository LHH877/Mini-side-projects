# Open the file "madlibs_generator_story.txt" in read mode and store its content in the variable 'story'
with open("madlibs_generator_story.txt", "r") as f:
    story = f.read()

# Create an empty set to store unique placeholder words
words = set()

# Initialize a variable to keep track of the starting index of a placeholder word
start_of_word = -1

# Define the characters that mark the start and end of a placeholder word
target_start = "<"
target_end = ">"

# Loop through each character in the story
for i, char in enumerate(story):
    # If the character is the starting mark of a placeholder word
    if char == target_start:
        start_of_word = i  # Record the starting index of the placeholder word

    # If the character is the ending mark of a placeholder word
    if char == target_end and start_of_word != -1:
        # Extract the placeholder word from the story
        word = story[start_of_word: i + 1]
        # Add the placeholder word to the set of unique words
        words.add(word)
        # Reset the starting index for the next placeholder word
        start_of_word = -1

# Create an empty dictionary to store user input for each placeholder word
answers = {}

# Prompt the user to enter a word for each placeholder word found in the story
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer  # Store the user input in the dictionary

# Replace each placeholder word in the story with the corresponding user input
for word in words:
    story = story.replace(word, answers[word])

# Print the modified story with user input filled in
print(story)
