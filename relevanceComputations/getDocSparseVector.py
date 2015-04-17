def getDocumentCorpus(directory):
    from nlpDoc import nlpDoc
    import wordDocumentHandlers
    #import nltk
    #from nltk.util import ngrams
    from nltk.tokenize import word_tokenize
    from gensim import corpora, models, similarities
    
    #This file will be used to transform a database of documents into the sparse 
    #vector representation required by Gensim's transformation models
    
    #Load documents
    #documents = a list of document objects which include metadata as well as a plaintext capture of the document
    docTexts = wordDocumentHandlers.importWordDocuments(directory)
    
    # remove common words and tokenize
    tokenizedTexts=[]
    for text in docTexts:
        tokenizedTexts.append(cleanAndTokenize(text))
        #wordCounts.append(nltk.FreqDist(word_tokenize(text)))

    #Create a set of documents each of which contains a tokenized text, a raw text, and a filename 
    documents = []
    for index, docText in enumerate(docTexts):
        currentDoc = nlpDoc(docText)
        currentDoc.tokenizedText = tokenizedTexts[index]
        currentDoc.documentType='Word' #Migrate this to the wordDocumentHandlers
        #currentDoc.filename = #[Can't do this until I fix the wordDocumentHandlers
        documents.append(currentDoc)
      
    return documents
    #return wordCounts
    #return sparseVecRepresentation
    
def fixString(text):
    import re
    text=text.encode('ascii','replace')
    return re.sub('[():;,.\'`\"1234567890?!]',' ',text)
    #Removes characters and converts to ascii
    #Need to add more to make this work better
    
def cleanAndTokenize(text):
    stoplist = set('an a and are as at be by for from has he in is it its of on that the to was were will with'.split())
    
    text = fixString(text)
    tokenizedText = [word for word in text.lower().split() if word not in stoplist]
    return tokenizedText