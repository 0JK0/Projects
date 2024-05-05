
def remove_duplicates(input_file, output_file):
    # Set to store unique words
    unique_words = set()

    # Read input file and process each word
    with open(input_file, 'r') as file:
        for line in file:
            word = line.strip()  # Remove leading/trailing whitespace
            unique_words.add(word)

    # Write unique words to output file
    with open(output_file, 'w') as file:
        for word in sorted(unique_words):  # Sort for consistent output
            file.write(word + '\n')

# Example usage
input_file = 'start.txt'
output_file = 'end.txt'
remove_duplicates(input_file, output_file)



