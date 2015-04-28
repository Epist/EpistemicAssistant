//Send requests to the server for suggested documents

function updateText(){
    
    if (typeof pastUserText !== 'undefined') {
     //the variable is defined
        currentUserText = document.getElementById("textEntry").value;
        stringDistance=getEditDistance(pastUserText,currentUserText);
        if (stringDistance>5){
            getSuggestions()
            pastUserText = currentUserText;
        }
        
    }
    else{
        pastUserText = document.getElementById("textEntry").value;
        getSuggestions()
    }
}
function getSuggestions(){
    $.ajax({

        // The URL for the request
        url: "/genSugg",

        // The data to send (will be converted to a query string)
        data: {
            inputText: document.getElementById("textEntry").value,
            numberOfDocs: '4'//Need to set the number of documents in a different way
        },

        // Whether this is a POST or GET request
        type: "GET",

        // The type of data we expect back
        //dataType : "json",

        // Code to run if the request succeeds;
        // the response is passed to the function
        success: function( responseData ) {
            generateSuggestionPanels(responseData);
            var panel = document.getElementById('testPanel');
            panel.innerHTML = responseData.texts[0];
            var title = document.getElementById('testTitle');
            title.innerHTML = responseData.titles[0];
            document.getElementById('testPanel2').innerHTML=responseData.texts[1]
            document.getElementById('testTitle2').innerHTML=responseData.titles[1]
        },

        // Code to run if the request fails; the raw request and
        // status codes are passed to the function
        error: function( xhr, status, errorThrown ) {
            alert( "Sorry, there was a problem!" );
            console.log( "Error: " + errorThrown );
            console.log( "Status: " + status );
            console.dir( xhr );
        },

        // Code to run regardless of success or failure
        //complete: function( xhr, status ) {
        //    alert( "The request is complete!" );
        //}
    });
}

//Algorithm from wikipedia for levenstein distance
// Compute the edit distance between the two given strings
function getEditDistance(a, b) {
  if(a.length === 0) return b.length; 
  if(b.length === 0) return a.length; 
 
  var matrix = [];
 
  // increment along the first column of each row
  var i;
  for(i = 0; i <= b.length; i++){
    matrix[i] = [i];
  }
 
  // increment each column in the first row
  var j;
  for(j = 0; j <= a.length; j++){
    matrix[0][j] = j;
  }
 
  // Fill in the rest of the matrix
  for(i = 1; i <= b.length; i++){
    for(j = 1; j <= a.length; j++){
      if(b.charAt(i-1) == a.charAt(j-1)){
        matrix[i][j] = matrix[i-1][j-1];
      } else {
        matrix[i][j] = Math.min(matrix[i-1][j-1] + 1, // substitution
                                Math.min(matrix[i][j-1] + 1, // insertion
                                         matrix[i-1][j] + 1)); // deletion
      }
    }
  }
 
  return matrix[b.length][a.length];
};
