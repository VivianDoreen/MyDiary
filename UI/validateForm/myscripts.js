var fulName = document.forms["vform"]["fullName"];
var userName = document.forms["vform"]["userName"];
var email = document.forms["vform"]["email"];
var password = document.forms["vform"]["password"];
var c_password = document.forms["vform"]["c_password"];

//Getting all error display objects
var name_error = document.getElementById('name_error');
var uname_error = document.getElementById('uname_error');
var email_error = document.getElementById('email_error');
var password_error = document.getElementById('password_error');
var c_password_error = document.getElementById('c_password_error');

//Settings all event Listners
fulName.addEventListener("blur", nameVerify, true);
userName.addEventListener("blur", uNameVerify, true);
email.addEventListener("blur", emailVerify, true);
password.addEventListener("blur", passwordVerify, true);

//Validation function
function validate(){
  //UserName Validation
  if (fulName.value == "") {
    fulName.style.border = "1px solid red";
    name_error.textContent = "UserName is required";
    fulName.forcus();
    return false;
  }
  //Email Validation
  if (email.value == "") {
    email.style.border = "1px solid red";
    email_error.textContent = "Email is required";
    email.forcus();
    return false;
  }
  //Email Validation
  if (password.value == "") {
    password.style.border = "1px solid red";
    password_error.textContent = "Password is required";
    password.forcus();
    return false;
  }
}
//Eventhandler functions
function nameVerify(){
  if (fulName.value != "") {
    fulName.style.border = "1px solid #000000";
    name_error.innerHTML = "";
    return true;

  }
}

function emailVerify(){
  if (email.value != "") {
    email.style.border = "1px solid #000000";
    email_error.innerHTML = "";
    return true;

  }
}

function passwordVerify(){
  if (c_password.value != "") {
    c_password.style.border = "1px solid #000000";
    c_password_error.innerHTML = "";
    return true;

  }
}
