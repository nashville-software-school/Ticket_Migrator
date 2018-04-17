"use strict";

let dragula_obj = dragula([
  document.getElementById("dragBoxLeft"),
  document.getElementById("dragBoxRight")
]);

$("#submit_button").click(e => {
    e.preventDefault();
    
  let results_container = $(dragula_obj.containers[0])[0].children
  let issue_array = Object.assign([], results_container).map((x, i) => { return { id: parseInt(x.id), priority: i }})
  let backlog_name = $("#backlog_name").val()
  let source_repo_id = $("#source_repo").val()

  let data = {"source_repo_id": source_repo_id, "backlog_name":backlog_name, "issue_array":issue_array}

  $.ajax({
    method: "POST",
    url: "./create_backlog",
    data: data
  }).done(backlog_id => {
    alert("Data Saved: " + msg);
  });

});
//convert jQuery collection to array - map to convert results to a array of objects {id, priority}
