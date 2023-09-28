function list() {
  var userName = document.getElementById("exampleInputEmail1").value;
  var pass = document.getElementById("exampleInputPassword1").value;
  let credentials = {"username": userName, "password": pass};
  console.log(credentials);
  test(credentials);
}

async function test(credentials) {
  var authToken = getCookie("authtoken");

  // Retrieve the CSRF token from the form
  var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

  try {
    var response = await fetch("http://127.0.0.1:8000/signin/", {
      method: 'POST',
      body: JSON.stringify(credentials),
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${authToken}`,
        'X-CSRFToken': csrfToken  // Include the CSRF token in the headers
      }
    });

    const obj = await response.json();
    console.log(obj);

    if (obj.is_valid) {
      console.log("Credentials are valid");
        window.location.href = "http://127.0.0.1:8000/home/";

      // Rest of your code here
    } else {
      console.log("Credentials are not valid");
    }
  } catch (error) {
    console.log(error);
  }
}
function getCookie(name) {

    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);

    if (parts.length === 2) return parts.pop().split(';').shift();

}

