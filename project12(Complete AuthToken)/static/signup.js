function list()
{
var userName = document.getElementById("exampleInputEmail1").value;
var pass = document.getElementById("exampleInputPassword1").value;
var credentials = {"username": userName, "password": pass}
test(credentials)
}


async function test(credentials) {

     // Retrieve the CSRF token from the form
  var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

  const response = await fetch('http://127.0.0.1:8000/signup/',
   {
    method: 'POST',
    body: JSON.stringify(credentials),
    headers: {
       'X-CSRFToken': csrfToken ,
      'Content-Type': 'application/json'
    }
  });
  const myJson = await response.json();
  console.log(myJson)
}