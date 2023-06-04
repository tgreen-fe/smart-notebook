function jsonInterpret()   
 {   
	
    var json = require('./testUpload.json'); //with path

    console.log(json[0])

    delete json[0]["fileName"]

    console.log(json[0])


         }  

jsonInterpret()