def mostRelevantDocs(textToCompare, numResults):
    """This function takes in a text string and a number of document results and
    returns the numResults most relevant documents to the text string using a predefined
    corpus and a hierarchical dirichlet process topic model
    
    Future functionality may include:
        - A way to change the corpus
        - A corpus stored on disk instead of in memory
        - A way to update the corpus without needing to fully recompute the model
        - A way to get similarity data without reloading and reforming the corpus
    """

    from gensim import corpora, models, similarities
    import logging
    from getDocSparseVector import *
    #reload(getDocSparseVector)
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #Use heirarchical dirichlet allocation topic modeling from gensim to compute the relevance between documents
    
    
    directory= "/Users/Larry/Code/EpistemicAssistant/sampleWordDocs/"
    #Imports a set of comparison documents and tokenizes them

    documents = getDocumentCorpus(directory) #Get document objects
    texts =[]
    for doc in documents:
        texts.append(doc.tokenizedText)
        #There has got to be a better way to do this...
    
    documentDictionary = corpora.Dictionary(texts)
    corpus = [documentDictionary.doc2bow(text) for text in texts]
    
    #Cleans and tokenizes the input text "cleanAndTokenize"
    mainDocument = documentDictionary.doc2bow(cleanAndTokenize(textToCompare))
                
    #Computes the HDA/nonparametric topic models
    hdp = models.HdpModel(corpus, id2word=documentDictionary)   
    corpusHdp = hdp[corpus]
    mainDocumentHdp = hdp[mainDocument]
    num_feat = len(documentDictionary.values()) #To get rid of warning, manually retreive dictionary feature size
    similarityIndex = similarities.MatrixSimilarity(corpusHdp, num_features=num_feat)
    sims = similarityIndex[mainDocumentHdp]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    
    topNum=numResults; #The number of documents to use as the top matches
    topSims=sims[0:topNum]
    topDocs = []
    for sims in topSims:
        topDocs.append(documents[sims[0]])
    return topDocs #returns the most relevant documents to the textToCompare
        