async function mist()
{
var authToken = getCookie("authtoken");


    try {

var response = await fetch("http://127.0.0.1:8000/home/", {

            method: 'GET',

            headers: {

                'Content-Type': 'application/json',

                'Authorization': `Token ${authToken}`

            }

        });
if (authToken)
{
console.log("Auth Token:", authToken)



}
else
{
console.log("Auth token not found")
}


    }
   catch (error) {

        console.log(error);

    }

}
//mist();


function getCookie(name) {

    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);

    if (parts.length === 2) return parts.pop().split(';').shift();

}