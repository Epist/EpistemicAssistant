def mostRelevantDocs(textToCompare, numResults, documents, corpus, documentDictionary, model):

    
    """This function takes in a text string and a number of document results and
    returns the numResults most relevant documents to the text string using a predefined
    corpus and a hierarchical dirichlet process topic model
    
    Future functionality may include:
        - A way to change the corpus
        - A corpus stored on disk instead of in memory
        - A way to update the corpus without needing to fully recompute the model
        - A way to get similarity data without reloading and reforming the corpus
        - A way to use n-grams and more complex features
        
    Package dependencies:
        - gensim
        
    """

    from gensim import similarities
    from getDocSparseVector import cleanAndTokenize
    #reload(getDocSparseVector)
    
    #Cleans and tokenizes the input text "cleanAndTokenize"
    mainDocument = documentDictionary.doc2bow(cleanAndTokenize(textToCompare))
                
     
    corpusModel = model[corpus]
    mainDocumentModel = model[mainDocument]
    num_feat = len(documentDictionary.values()) #To get rid of warning, manually retreive dictionary feature size
    similarityIndex = similarities.MatrixSimilarity(corpusModel, num_features=num_feat)
    sims = similarityIndex[mainDocumentModel]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    
    topNum=numResults; #The number of documents to use as the top matches
    topSims=sims[0:topNum]
    topDocs = []
    for sims in topSims:
        topDocs.append(documents[sims[0]])
    return topDocs #returns the most relevant documents to the textToCompare
        