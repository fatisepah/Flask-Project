$(document).ready(function () {
  let switcher = $(".switcher");
  let signup_section = $(".signup");
  let signin_section = $(".sign-in");
  switcher.click(function () {
    let value = switcher.html();
    if (value == "Sign in") {
      signup_section.fadeOut();
      signin_section.fadeIn();
      switcher.html("Sign up");
    } else {
      // is Sign Up
      signin_section.fadeOut();
      signup_section.fadeIn();
      switcher.html("Sign in");
    }
  });
});
