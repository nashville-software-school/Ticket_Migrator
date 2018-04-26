// Triggered on button click - adds another text input for target repos
// Regex pattern checks that it starts with https:///github.com and then has something
// that looks like camilleryr/bandstagram after it
const addInput = () => {
  $("#target_repos_div").append(
    $(`
        <input
            class="input target_repos_inputs" 
            type="text" 
            name="source_repo" 
            pattern='^https:\\/\\/github.com\\/\\S*\\/\\S*(?<!/)'
            title="Use full url with no whitespace - IE : https://github.com/PythonWizards/MigratorTesting"
            placeholder="https://github.com/PythonWizards/MigratorTesting"
            >
    `)
  );
};

// Run on form submission to validate auth token and scrape values from input fields
const set_form_values = () => {
  //Check for presence of auth token and fail form submission if not present
  if (!get_auth_token()) {
    $("#ErrorHandler").toggleClass("is-active");
    $("#ErrorMessage").html("Please make sure you have saved a token to local storage");
    return false;
  }

  //Check for some number of target repos and fail form submission if not present
  if (!get_target_repo_value()) {
    $("#ErrorHandler").toggleClass("is-active");
    $("#ErrorMessage").html("Please make sure you have entered in target repos");
    return false;
  }

  show_loading_gif_modal();

  // Return true to trigger form submission
  return true;
};

const show_loading_gif_modal = () => {
  $("#gifModal").toggleClass("is-active");
};

// Query all of the target repo input fields convert the html collection into an array
// pull out the doman from the target repos entered discard the null values and set the results
// to a form input so it can be submitted to the server
// Return a bool value is equivelent to is there value?
const get_target_repo_value = () => {
  return ($("#target_repos")[0].value = JSON.stringify(
    Object.assign([], $(".target_repos_inputs"))
      .map(x => x.value.split("https://github.com/")[1])
      .filter(x => x != null)
  )) != "[]"
    ? true
    : false;
};

// Set the value of the "Authorization" key from local storage to a form value so it can
// be submitted to the server - return a bool value that reflects if the token was present
const get_auth_token = () => {
  return ($("#credentials")[0].value = JSON.parse(
    localStorage.getItem("Authorization")
  )) != null
    ? true
    : false;
};

// Trigger the addInput function on button click
$("#add").click(e => addInput());

// Populate the dom with a single input on page load
$(document).ready(addInput());
