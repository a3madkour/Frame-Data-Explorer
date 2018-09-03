var fs = require('fs');
fs.readFile('tekken7Data/paul-basic.json', 'utf8', function (err, data) {
    if (err) throw err; 
    var obj = JSON.parse(data);
    for (var i in obj){
        console.log(obj[i].Command);
        break;
    }
});

