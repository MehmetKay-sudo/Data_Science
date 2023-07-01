import pandas as pd
from collections import Counter

# Read the text file
with open('/path/to/file', 'r') as file:
    text = file.read()

# Preprocess the text (optional, if needed)
# Remove punctuation, convert to lowercase, etc.

# Split the text into individual words
words = text.split()

# Count the word frequencies
word_freq = Counter(words)

# Convert the word frequencies to a DataFrame
df = pd.DataFrame.from_dict(word_freq, orient='index', 
columns=['Frequency'])

# Sort the DataFrame by frequency in descending order
df = df.sort_values('Frequency', ascending=False)

# Save the DataFrame as a CSV file
df.to_csv('/path/to/file', index_label='Word')

