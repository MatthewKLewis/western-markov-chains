import random
import re as regex
from collections import defaultdict

# Import the text from the path listed.
path = 'westerns.txt'

# Opening the file and assigning it 'textFile', pull the text into a string.
with open(path) as textFile:
    westernText = textFile.read()

# Remove all line breaks from the text
westernText = westernText.replace('\r', ' ').replace('\n', ' ').replace('"', " ").replace('.', ' ').replace(';', ' ').replace(',', '').replace('_', "").replace('  ', ' ')

# Split the text into individual words, formed as a list. 
# '\W+' is a regular expression targeting words with one or more characters
# textAsList = [word for word in regex.split('\W+', westernText) ]

# Split the text into word couplets, formed as a list
textAsList = [word for word in regex.split(' ', westernText) ]

# Create the Dictionary
westernMarkovDictionary = defaultdict(lambda: defaultdict(int))

#Start the last word as the first word in the list, make it lowercase.
last_word = textAsList[0].lower()

#For each word in the list, make it lowercase, and set the preceding word as a key to find that word
for word in textAsList[1:]:
  word = word.lower()
  westernMarkovDictionary[last_word][word] += 1
  last_word = word

# The sample string starts with a random word from the textList
sampleString =  random.choice(textAsList)

# and the last word in the string is set to that word
lastWord = sampleString

# from 0 to n, the string is appended with a random choice from potential following words
i = 0
while i < 40:
    tempWord = random.choice(list(westernMarkovDictionary[lastWord].keys()))
    sampleString += ' ' + tempWord
    lastWord = tempWord
    i += 1

# and the string is printed!
print(sampleString)