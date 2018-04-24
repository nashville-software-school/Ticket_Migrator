const addInput = () => {
    $('#target_repos_div').append($(`
        <input
            class="input target_repos_inputs" 
            type="text" 
            name="source_repo" 
            pattern='^https:\\/\\/github.com\\/\\S*\\/\\S*(?<!/)'
            title="Use full url with no whitespace - IE : https://github.com/PythonWizards/MigratorTesting"
            placeholder="https://github.com/PythonWizards/MigratorTesting"
            >
    `))
}

const set_form_values = () => {
    // const userToken = JSON.parse(localStorage.getItem("Authorization"))
    
    // //check for token
    // if ( userToken === userToken) {
    //     //Proceed with Success
    //   } else if (userToken === null) {
    //       return console.log("Unable to get Token from local Storage");
    //   }
    //if none alert "set token" return false

    get_target_repo_value()
    if($('#target_repos')[0].value == "[]")
    {
        return false
    }
    get_credentails()
    show_loading_gif_modal()
    return true
}

const show_loading_gif_modal = () => {
    $('#gifModal').toggleClass('is-active');
}

const get_target_repo_value = () => {
    $('#target_repos')[0].value = 
        JSON.stringify(Object.assign([], $('.target_repos_inputs'))
        .map(x => x.value.split("https://github.com/")[1])
        .filter(x => x != null))
}

const get_credentails = () => {
    $('#credentials')[0].value = 
        btoa($('#username').first().val() + ":" + $('#password').first().val())
}

$('#add').click(e => addInput())

$(document).ready(addInput())

