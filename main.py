import re
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

count = 0
sentenceCounter = 1
file = open("input.txt", "r")
sentenceFile = open("sentimentAnalysisPerSentence.txt", "w")
Lines = file.readlines()

for line in Lines:
    sentenceFile.writelines("Polarity and sentiment of line " + str(sentenceCounter) + " is " + str(TextBlob(line).sentiment.polarity) + " and " + str(TextBlob(line).sentiment.subjectivity) + "\n")
    sentenceCounter += 1


with open("input.txt", "r") as testFile:
    textFile = testFile.read()


print(TextBlob(textFile).sentiment)

testFile.close()
