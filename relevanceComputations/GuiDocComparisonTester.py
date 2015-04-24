#Gui Document Comparison Topic Modeling tester
from mostRelevantDocs import *

textToCompare = raw_input('Enter some text: ')

numResults = 5

topDocs = mostRelevantDocs(textToCompare, numResults)

docTexts = []
for doc in topDocs:
    docTexts.append(doc.rawText)
    
print "Best result:\n"
firstThousandChars=docTexts[0][0:999]
print firstThousandChars