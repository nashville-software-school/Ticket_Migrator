"use strict";

let dragula_obj = dragula([
  document.getElementById("dragBoxLeft"),
  document.getElementById("dragBoxRight")
]);

let saved_backlog = null
let results_container = $(dragula_obj.containers[0])[0].children

$("#home_button").click(e => {
    window.location.href = "../"
})

$("#migrate_button").click(e => {
    window.location.href = `../migrate/${saved_backlog}`
})

$("#create_button").click(e => {
    $(".modal").removeClass('is-active')
    $("#backlog_name")[0].value = ''
    let r = $('.issue').remove()
    $(dragula_obj.containers[1]).append(r)

})

$("#submit_button").click(e => {
    e.preventDefault();
    
  let issue_array = JSON.stringify(Object.assign([], results_container).map((x, i) => { return { id: parseInt(x.id), priority: i }}))
  let backlog_name = $("#backlog_name").val()
  let source_repo_id = $("#source_repo").val()

  let data = {"source_repo_id": source_repo_id, "backlog_name":backlog_name, "issue_array":issue_array}

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

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
    url: "../createbacklog/",
    data: data
  }).done(response => {
    saved_backlog = response.backlog_id
    $(".modal").addclass('is-active')
  });

});
//convert jQuery collection to array - map to convert results to a array of objects {id, priority}
