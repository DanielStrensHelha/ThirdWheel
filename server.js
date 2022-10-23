var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
const PORT = 8080;

app.use(express.static('public'));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/public/index.html');
});

io.on('connection', function(socket) {
    console.log('A user connected');
    socket.emit('youreConnected', 'you are connected, try to display this message.');
});

http.listen(PORT, function() {
    console.log('app oppened on port 3000');
});