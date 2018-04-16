const addInput = () => {
    $('#target_repos_div').append($("<input class='target_repos_inputs' type='text' name='username' placeholder='ie https://github.com/username/repo'>"))
}

const set_form_values = () => {
    get_target_repo_value()
    get_credentails()
    return true
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

