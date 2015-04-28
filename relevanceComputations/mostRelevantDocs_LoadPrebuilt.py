def mostRelevantDocs(textToCompare, numResults):

    
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

    from gensim import corpora, models, similarities
    import logging
    from getDocSparseVector import getDocumentCorpus, cleanAndTokenize
    import cPickle as pickle

    #reload(getDocSparseVector)
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #Use heirarchical dirichlet allocation topic modeling from gensim to compute the relevance between documents
    
    
    documentDictionary = pickle.load(open("/Users/Larry/Code/EpistemicAssistant/relevanceComputations/documentDictionary.p", "rb"))#load document dictionary
    corpus = pickle.load(open("/Users/Larry/Code/EpistemicAssistant/relevanceComputations/corpus.p", "rb")) #load corpus
    hdp = pickle.load(open("/Users/Larry/Code/EpistemicAssistant/relevanceComputations/hdp.p", "rb"))#load hdp model
    documents = pickle.load(open("/Users/Larry/Code/EpistemicAssistant/relevanceComputations/documents.p", "rb"))#load documents
    
    #Cleans and tokenizes the input text "cleanAndTokenize"
    mainDocument = documentDictionary.doc2bow(cleanAndTokenize(textToCompare))
     
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
        