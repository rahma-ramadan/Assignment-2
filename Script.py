import re  # Import the regular expression module
from collections import Counter  # Import the Counter class for counting frequencies
from nltk.corpus import stopwords  # Import NLTK's stopwords corpus
import nltk  # Import NLTK

# Download NLTK stop words if not already downloaded
nltk.download('stopwords')

# Read the content of the file
with open("random_paragraphs.txt", 'r') as file:
    text = file.read()

# Get a set of English stopwords
stop_words = set(stopwords.words('english'))

# Tokenize text into words using regular expression
words = re.findall(r'\b\w+\b', text.lower())  

# Filter out stopwords
filtered_words = [word for word in words if word not in stop_words]

# Count word frequency
word_counts = Counter(filtered_words)

# Print word frequency
print("Word Frequency:")
for word, count in word_counts.most_common():
    print(f"{word}: {count}")  # Print each word along with its frequency
