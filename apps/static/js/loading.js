function loading_login(button, email, password) {
  if (document.getElementById("login_form").checkValidity()) {
    document.getElementById(button).setAttribute("aria-busy", "true");
    document.getElementById(email).setAttribute("aria-invalid", "false");
    document.getElementById(password).setAttribute("aria-invalid", "false");
  } else {
    document.getElementById(button).setAttribute("aria-busy", "false");
    document.getElementById(email).setAttribute("aria-invalid", "true");
    document.getElementById(password).setAttribute("aria-invalid", "true");
  }
}
