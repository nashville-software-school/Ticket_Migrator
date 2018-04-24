//This function supposedly handles adding a token to local storage from the
// input box in layout.html. Checks for any matches and nulls
checkToken = () => {
  const addToken = document.getElementById('token_input_field').value;
  const getToken = JSON.parse(localStorage.getItem('Authorization'));
debugger
  if (addToken != getToken && addToken != null) {
      localStorage.setItem("Authorization", JSON.stringify(addToken))
    $('#toke_new').toggleClass('is-active');
    return console.log('token went in');
  } else if (addToken === getToken) {
    return console.log('Sorry Dave, I already have that Token in my memory.');
  } else if (addToken === null) {
    return console.log('Gotta put somethin good in here');
  }
};
