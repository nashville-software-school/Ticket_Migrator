//This function supposedly handles adding a token to local storage from the
// input box in layout.html. Checks for any matches and nulls
$('#auth_false_show').show()
$('#auth_true_show').hide()

checkToken = () => {
    // set the value of the fireld and the value of the localstorage, if any, into variables.
    const tokenInputValue = document.getElementById('token_input_field').value;
    const tokenAlreadyStored = JSON.parse(localStorage.getItem('Authorization'));
    
    if (tokenInputValue != tokenAlreadyStored && tokenInputValue != null) {
        //throw it in
        localStorage.setItem('Authorization', JSON.stringify(tokenInputValue));
        //this willeventually hide/show the input field or whetever we use to show an authenticated user
        $('#auth_false_show').hide()
        $('#auth_true_show').show()
    // c-log for developer info
    return console.log('token that went in:', tokenInputValue);
    //check if the token is equal to the one in localstorage, this is reduntant with the addition of hide/show logic
    } else if (tokenInputValue === tokenAlreadyStored) {
        // c-log for developer info
        return console.log('Sorry Dave, I already have that Token in my memory.');
        //check to see if the input box is null, throw an error.
    } else if (tokenInputValue === null) {
        // c-log for developer info
        return console.log('Gotta put somethin good in here');
    }
};
