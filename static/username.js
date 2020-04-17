document.addEventListener('DOMContentLoaded', function() {
    let username = localStorage.getItem('name')
    document.querySelector('#username').innerHTML = username;

});
