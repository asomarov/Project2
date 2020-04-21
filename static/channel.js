document.addEventListener('DOMContentLoaded', function() {

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    socket.on('connect', () => {

      document.querySelector('#message_form').onsubmit = function() {
        const message = document.querySelector('#message').value
        socket.emit('send message', {'message': message});
      };
    });


    socket.on('announce message', data => {
        const li = document.createElement('li');
        li.innerHTML = `${data.message}`;
        document.querySelector('#messages').append(li);
    });
});
