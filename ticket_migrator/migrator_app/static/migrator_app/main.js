//This function supposedly handles adding a token to local storage from the
// input box in layout.html. Checks for any matches and nulls
checkToken = () => {
  // set the value of the fireld and the value of the localstorage, if any, into variables.
  const tokenInputValue = document.getElementById('token_input_field').value;
  const tokenAlreadyStored = JSON.parse(localStorage.getItem('Authorization'));

  if (
    (tokenInputValue != tokenAlreadyStored && tokenInputValue != null) ||
    tokenInputValue === tokenAlreadyStored
  ) {
    //throw it in
    localStorage.setItem('Authorization', JSON.stringify(tokenInputValue));
    $('#token_field_submit').click(e => {
      $("#auth_true_show'").toggleClass('is-active');
    });
    console.log('token that was just saved: ', tokenInputValue);
  } else if (tokenInputValue === null) {
    $('#token_field_submit').click(e => {
      $("#auth_false_show'").toggleClass('is-active');
    });
    console.log('You are null');
  }
};

// else if (tokenInputValue === tokenAlreadyStored) {
//     hideShowFunction.showAuthorized();
//     // c-log for developer info
//      console.log('Welcome Returning user: ', tokenAlreadyStored);
//     //check to see if the input box is null, throw an error.
// }
