if (!localStorage.getItem('name'))
  localStorage.setItem('name',"");

  document.addEventListener('DOMContentLoaded', function() {
      let username = localStorage.getItem('name')
      document.querySelector('#greeting').innerHTML = `Hello ${username}`;

      document.querySelector('#form').onsubmit = function() {
          const name = document.querySelector('#name').value;
          localStorage.setItem('name', name);
      };
  });
