def getDocumentCorpus(directory):
    from nlpDoc import nlpDoc
    import wordDocumentHandlers
    import nltk
    #from nltk.util import ngrams
    from nltk.tokenize import word_tokenize
    from gensim import corpora, models, similarities
    
    #This file will be used to transform a database of documents into the sparse 
    #vector representation required by Gensim's transformation models
    
    #Load documents
    #documents = a list of document objects which include metadata as well as a plaintext capture of the document
    docTexts = wordDocumentHandlers.importWordDocuments(directory)
    
    # remove common words and tokenize
    stoplist = set('for an a of the and to in it is '.split())
    
    wordCounts = []
    fixedTexts=[]
    #Count word frequencies
    #ngramMax=1;
    for text in docTexts:
        #Build a dictionary or a hashmap of the word counts
        fixedTexts.append(fixString(text))
        #wordCounts.append(nltk.FreqDist(word_tokenize(text)))
        
    tokenizedTexts = [[word for word in document.lower().split() if word not in stoplist]
            for document in fixedTexts]
        

    #Want to create a set of documents each of which contains a tokenized text, a raw text, and a filename 
    documents = []
    for index, docText in enumerate(docTexts):
        currentDoc = nlpDoc(docText)
        currentDoc.tokenizedText = tokenizedTexts[index]
        #currentDoc.filename = 
        documents.append(currentDoc)
      
    return documents
    #return wordCounts
    #return sparseVecRepresentation
    
def fixString(text):
    import re
    text=text.encode('ascii','replace')
    return re.sub('[():;,.\'`\"1234567890?!]',' ',text)
    #Removes characters 
    #Use str() to transform from unicode to ASCII
    #Need to add more to make this work better