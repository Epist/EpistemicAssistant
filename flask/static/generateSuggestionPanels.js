function generateSuggestionPanels(responseData){
    var leftSideHtml=''
    var rightSideHtml=''
    
    //Build sidebar html from responseData
    
    //Choose panel type based on document type
    
    //Assign the sidebar html to the sidebar innerhtml elements
    
    numPanels = responseData.texts.length;
    for (i=0; i<numPanels; i++){
        if (i % 2 == 0){ //Alternate sidebars to assign panels to
            var currentSidebar = leftSideHtml;
        }
        else{
            currentSidebar = rightSideHtml;
        }
        if (responseData.docTypes[i] == 'MS Word'){
            currentSidebar += '<div class="panel panel-success">'
        }
        else if (responseData.docTypes[i] == 'Reuters'){
            currentSidebar += '<div class="panel panel-info">'
        }
        else if (responseData.docTypes[i] == 'PDF'){
            currentSidebar += '<div class="panel panel-warning">'
        }
        else{
            currentSidebar += '<div class="panel panel-default">'
        }
        currentSidebar +=  '<div class="panel-heading">' +
                        '<h3 class="panel-title" id="testTitle">';
        currentSidebar += responseData.titles[i];
        currentSidebar +=  '</h3>' +
                    '</div>' +
                    '<div class="panel-body" id="testPanel">';
        currentSidebar += responseData.texts[i];
        currentSidebar +=     '</div>' +
                '</div>';
        
        if (i % 2 == 0){ //Save to sidebar for completion
            leftSideHtml = currentSidebar;
        }
        else{
            rightSideHtml = currentSidebar;
        }  
            
    }
    document.getElementById('leftSuggestionColumn').innerHTML=leftSideHtml;
    document.getElementById('rightSuggestionColumn').innerHTML=rightSideHtml;
    
}