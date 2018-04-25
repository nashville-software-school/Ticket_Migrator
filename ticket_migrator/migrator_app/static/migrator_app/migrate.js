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

const set_form_values = () => {
  if (!get_auth_token()) {
    alert("Please make sure you have saved a token to local storage");
    return false;
  }

  if (!get_target_repo_value()) {
    alert("Please make sure you have entered in target repos");
    return false;
  }

  show_loading_gif_modal();
  return true;
};

const show_loading_gif_modal = () => {
  $("#gifModal").toggleClass("is-active");
};

const get_target_repo_value = () => {
  return ($("#target_repos")[0].value = JSON.stringify(
    Object.assign([], $(".target_repos_inputs"))
      .map(x => x.value.split("https://github.com/")[1])
      .filter(x => x != null)
  )) != "[]"
    ? true
    : false;
};

const get_auth_token = () => {
  return ($("#credentials")[0].value = JSON.parse(
    localStorage.getItem("Authorization")
  )) != null
    ? true
    : false;
};

$("#add").click(e => addInput());

$(document).ready(addInput());
