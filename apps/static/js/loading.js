function loading_login(button, email, password, remember_me) {
  if (document.getElementById("login_form").checkValidity()) {
    document.getElementById(button).setAttribute("disabled", "disabled");
    let spinner = document.createElement("span");
    spinner.setAttribute("class", "spinner-border spinner-border-sm");
    spinner.setAttribute("aria-hidden", "true");
    document.getElementById(button).appendChild(spinner);
    document.getElementById(remember_me).setAttribute("disabled", "disabled");
    document
      .getElementById(email)
      .setAttribute("class", "form-control is-valid");
    document
      .getElementById(password)
      .setAttribute("class", "form-control is-valid");
  } else {
    document.getElementById(button).removeAttribute("disabled");
    document.getElementById(remember_me).removeAttribute("disabled");
    document
      .getElementById(email)
      .setAttribute("class", "form-control is-invalid");
    document
      .getElementById(password)
      .setAttribute("class", "form-control is-invalid");
  }
}
