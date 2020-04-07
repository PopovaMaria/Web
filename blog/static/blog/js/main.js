  function on_ready()
  {
    var input = document.getElementById('id_password');

    input.oninput = function()
    {
    if (!(input.value.match(/\d/)))

        document.getElementById('2').innerHTML = 'Пароль должен содержать цифры';
    else
            document.getElementById('2').innerHTML = ' ';


  }
  }
  document.addEventListener("DOMContentLoaded", on_ready);
