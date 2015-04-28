#The goal is to create something that connects my NLP functions with my web-based front end
import sys
sys.path.append('/Users/Larry/Code/EpistemicAssistant/relevanceComputations/')

from flask import Flask, jsonify, render_template, request

from mostRelevantDocs_prebuiltAsArgs import mostRelevantDocs
from startNLPOperations import startNLP, startNLP_load

app = Flask(__name__, static_folder='/Users/Larry/Code/EpistemicAssistant/flask/static', template_folder='/Users/Larry/Code/EpistemicAssistant/flask/templates')

#@app.route('/')
#def hello_world():
#    return 'Hello World!'
    
#@url_for('static', filename='BootstrapTest.html')

#To rebuild the corpus, use startNLP; to load an existing corpus, use startNLP_load
NLPvars = startNLP('tfidf')#Start the NLP processes using a model set by the parameter
#Model Types are 'tfidf', 'hdp', 'lda' 

global documents, corpus, documentDictionary, hdp
documents = NLPvars['documents']
corpus = NLPvars['corpus']
documentDictionary = NLPvars['documentDictionary']
currentModel = NLPvars['currentModel']

@app.route('/')
def test():
    return render_template('BootstrapTest.html')
    

@app.route('/genSugg')
def genSugg():
    #global documents, corpus, documentDictionary, hdp
    textToCompare=request.args.get('inputText','0')
    numItems = request.args.get('numberOfDocs','0')
    numItems = int(float(numItems))
    #numItems=5#Number of documents to return
    titleSuggestions=[]
    textSuggestions=[]
    suggestions = mostRelevantDocs(textToCompare, numItems, documents, corpus, documentDictionary, currentModel)
    for i in range(numItems):
        textSuggestions.append(suggestions[i].rawText[0:199])#Just for testing purposes
        docTitle = suggestions[i].documentType
        titleSuggestions.append(docTitle + ': ' + suggestions[i].filename)
    return jsonify(texts=textSuggestions, titles=titleSuggestions)
                

if __name__ == '__main__':
    app.run(debug = True)
        