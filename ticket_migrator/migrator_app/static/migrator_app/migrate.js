let Validate = () =>
  Object.create(null, {
    array: { value: [], writable: true, enumerable: true },
    add: {
      value: function(repo) {
        this.array.push(repo);
        return repo;
      }
    },
    validate: {
      value: function(form) {
        let apistring =
          "https://spyproxy.bangazon.com/student/commit/https://api.github.com/repos/";
        Promise.all(
          this.array.map(x => apistring + x).map(x => $.ajax((url = x)))
        ).then(
          (success = res => {
            if (res.every(x => x.hasOwnProperty("id"))) {
              show_loading_gif_modal();
              form.submit();
              return true;
            } else {
              alert("Not all target repos are valid");
              return false;
            }
          }),
          (fail = res => {
            alert("Not all target repos are valid");
            return false;
          })
        );
      }
    }
  });

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
const set_form_values = form => {
  //Check for some number of target repos and fail form submission if not present
  let validator = get_target_repo_value();
  if (!validator) {
    alert("Please make sure you have entered in target repos");
    return false;
  }

  if (!get_passphrase()) {
    alert("Please make sure you enter a secrete token passphrase");
    return false;
  }

  validator.validate(form);

  return false;
};

const show_loading_gif_modal = () => {
  $("#gifModal").toggleClass("is-active");
};

// Query all of the target repo input fields convert the html collection into an array
// pull out the doman from the target repos entered discard the null values and set the results
// to a form input so it can be submitted to the server
// Return a bool value is equivelent to is there value?
const get_target_repo_value = () => {
  let validator = Validate();
  return ($("#target_repos")[0].value = JSON.stringify(
    Object.assign([], $(".target_repos_inputs"))
      .map(x => x.value.split("https://github.com/")[1])
      .filter(x => x != null)
      .map(x => validator.add(x))
  )) != "[]"
    ? validator
    : false;
};

// Set the value of the "Authorization" key from local storage to a form value so it can
// be submitted to the server - return a bool value that reflects if the token was present
const get_passphrase = () => {
  return ![null, ""].includes(
    ($("#credentials")[0].value = prompt(
      "Enter Token Passphrase",
      "Super Secret Passphrase"
    ))
  );
};

// Trigger the addInput function on button click
$("#add").click(e => addInput());
$("#target_repos_div").keyup(e => {
  if (e.target == $("#target_repos_div > :last")[0]) {
    addInput();
  }
});

// Populate the dom with a single input on page load
$(document).ready(addInput());
