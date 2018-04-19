function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

const delete_repo = (id) => {
    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    
    $.ajax({
        method: "POST",
        url: `../delete_repo/${id}`
    }).done(response => {
        location.reload()
    });
}

$(".delete").click(e => {
    let sr_id = e.target.id
    let sr_url = $(`.sr-${sr_id }`)[0].innerHTML
    $("#backlog_url")[0].innerHTML = sr_url
    $(".modal").toggleClass('is-active')
    $("#confirm").click(e => delete_repo(sr_id))
})

$(".hide_modal_button").click(e =>  {
    $(".modal").toggleClass('is-active')
    $("#confirm").off('click')
})