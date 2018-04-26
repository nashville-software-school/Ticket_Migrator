// Saves the value of the token_input_field to local storage
// hides the input field and shows the "authorized" div
// returns false to stop the form from being submitted
const addToken = () => {
  const tokenInputValue = document.getElementById("token_input_field").value;
  localStorage.setItem("Authorization", JSON.stringify(tokenInputValue));
  swap_displayed_div();
  return false;
};

// Removes the token from local storage
// hides the "authorized" div and shows the input field
// returns false to stop the form from being submitted
const removeToken = () => {
  localStorage.removeItem("Authorization");
  swap_displayed_div();
  return false;
};

const swap_displayed_div = () => {
  $(".header--auth").toggleClass("hidden");
};

// Checks for the presence of a token and returns a bool value
const verify_token = () => {
  return JSON.parse(localStorage.getItem("Authorization")) != null
    ? true
    : false;
};

// On page load - interpolate the bool value returned from verify token function
// to show the appropriate auth div
$(document).ready(() =>
  $(`#auth_${verify_token()}_show`).toggleClass("hidden")
);
