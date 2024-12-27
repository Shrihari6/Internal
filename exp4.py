# Program to count occurrences of a letter in a file
fname = input("Enter the file name: ")
ltr = input("Enter the letter to be searched: ")
k = 0

try:
    # Open the file in read mode
    with open(fname, 'r') as fptr:
        for line in fptr:  # Read each line
            words = line.split()  # Split line into words
            for word in words:  # Iterate over each word
                for letter in word:  # Iterate over each letter
                    if letter == ltr:  # Check if letter matches
                        k += 1

    print(f"Occurrences of the letter '{ltr}': {k}")

except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print(f"An error occurred: {e}")