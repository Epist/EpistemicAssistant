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
    return render_template('EpistemicAssistantPen.html')
    

@app.route('/genSugg')
def genSugg():
    #global documents, corpus, documentDictionary, hdp
    textToCompare=request.args.get('inputText','0')
    numItems = request.args.get('numberOfDocs','0')
    numItems = int(float(numItems))
    #numItems=5#Number of documents to return
    titleSuggestions=[]
    textSuggestions=[]
    docTypes=[]
    suggestions = mostRelevantDocs(textToCompare, numItems, documents, corpus, documentDictionary, currentModel)
    for i in range(numItems):
        currentSuggestion=smart_truncate(suggestions[i].rawText, 250)#Maybe play with the truncation size
        textSuggestions.append(currentSuggestion)
        docTitle = suggestions[i].documentType
        titleSuggestions.append(docTitle + ': ' + suggestions[i].filename)
        docTypes.append(suggestions[i].documentType)
    return jsonify(texts=textSuggestions, titles=titleSuggestions, docTypes=docTypes)
     
#Move this function somewhere else    
def smart_truncate(content, length, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix
                

if __name__ == '__main__':
    app.run(debug = True)
        