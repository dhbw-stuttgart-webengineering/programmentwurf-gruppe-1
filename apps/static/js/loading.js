function loading_login(button, email, password, rememberme) {
  if (document.getElementById("login_form").checkValidity()) {
    form = document.getElementById("login_form");
    document.getElementById(button).setAttribute("disabled", "disabled");
    let spinner = document.createElement("span");
    spinner.setAttribute("class", "spinner-border spinner-border-sm");
    spinner.setAttribute("aria-hidden", "true");
    document.getElementById(button).appendChild(spinner);
    document.getElementById(rememberme).setAttribute("disabled", "disabled");
    document
      .getElementById(email)
      .setAttribute("class", "form-control is-valid");
    document
      .getElementById(password)
      .setAttribute("class", "form-control is-valid");
    form.submit();
  } else {
    document.getElementById(button).removeAttribute("disabled");
    document.getElementById(rememberme).removeAttribute("disabled");
    document
      .getElementById(email)
      .setAttribute("class", "form-control is-invalid");
    document
      .getElementById(password)
      .setAttribute("class", "form-control is-invalid");
  }
}


function guest_login() {
  document.getElementById("email").value = "example@lehre.dhbw-stuttgart.de";
  document.getElementById("password").value = "You found the example password!";
  document.getElementById("submit_login").click();
}