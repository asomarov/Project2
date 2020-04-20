
  document.addEventListener('DOMContentLoaded', function() {
      document.querySelector('#form').onsubmit = function() {
          let name = document.querySelector('#name').value;
          localStorage.setItem('name', name);
      };
  }
