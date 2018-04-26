//This function supposedly handles adding a token to local storage from the
// input box in layout.html. Checks for any matches and nulls
const addToken = () => {
  // set the value of the fireld and the value of the localstorage, if any, into variables.
  const tokenInputValue = document.getElementById("token_input_field").value;
  //throw it in
  localStorage.setItem("Authorization", JSON.stringify(tokenInputValue));

  swap_displayed_div();

  return false;
};

const removeToken = () => {
  localStorage.removeItem("Authorization");
  swap_displayed_div();
  return false;
};

const swap_displayed_div = () => {
  $(".header--auth").toggleClass("hidden"); 
};

const verify_token = () => {
  return JSON.parse(localStorage.getItem("Authorization")) != null
    ? true
    : false;
};

$(document).ready(() => {
  if (verify_token()) {
    $("#auth_true_show").toggleClass("hidden");
  } else {
    $("#auth_false_show").toggleClass("hidden");
  }
});

// Warning box functionality i dunno
// const removeWarningBox = () => {
//   $("#ErrorHandler").click(e => {
//   $(".delete").removeClass('hidden')
// })}

// else if (tokenInputValue === tokenAlreadyStored) {
//     hideShowFunction.showAuthorized();
//     // c-log for developer info
//      console.log('Welcome Returning user: ', tokenAlreadyStored);
//     //check to see if the input box is null, throw an error.
// }
