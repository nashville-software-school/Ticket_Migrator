$(".delete").click(e => {
    let sr_id = e.target.id
    let sr_url = $(`.sr-${sr_id }`)[0].innerHTML
    $("#backlog_url")[0].innerHTML = sr_url
    $(".modal").toggleClass('is-active')
    $("#confirm").attr('href',`../delete_repo/${sr_id}`)
})

$(".hide_modal_button").click(e =>  {
    $(".modal").toggleClass('is-active')
    $("#confirm").attr('href','')
})