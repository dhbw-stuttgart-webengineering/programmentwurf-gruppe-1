function loading(id) {
  if (document.getElementById("login_form").checkValidity()) {
    document.getElementById(id).setAttribute("aria-busy", "true");
  } else {
    document.getElementById(id).setAttribute("aria-busy", "false");
  }
}
