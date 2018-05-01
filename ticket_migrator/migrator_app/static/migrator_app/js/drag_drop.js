"use strict";

// Initialize dragulajs
let dragula_obj = dragula([
  document.getElementById("dragBoxLeft"),
  document.getElementById("dragBoxRight")
]);

let saved_sprint = null;
let results_container = $(dragula_obj.containers[0])[0].children;

// Go home
$("#home_button").click(e => {
  window.location.href = "../";
});

// Go to the migrate page of the just saved sprint
$("#migrate_button").click(e => {
  window.location.href = `../migrate/${saved_sprint}`;
});

// Resets the page so you can create an additional sprint
$("#create_button").click(e => {
  $(".modal").removeClass("is-active");
  $("#sprint_name")[0].value = "";
  // query all issue divs
  let r = $(".issue").remove();
  // move all of them issue divs to the right column
  $(dragula_obj.containers[1]).append(r);
});

// Close the modal
$("#modal-close").click(e => {
  $(".modal").removeClass("is-active");
});

// Function is triggered on form submission
const on_submit = () => {
  // Query all issue divs in the left hand column - convert the html collection into an array -
  // Map over the array and return an array of objects with the GITHUB ID and PRIORITY
  let issue_array = JSON.stringify(
    Object.assign([], results_container).map((x, i) => {
      return { id: parseInt(x.id), priority: i };
    })
  );
  let sprint_name = $("#sprint_name").val();
  let source_repo_id = $("#source_repo").val();

  if (issue_array === "[]") {
    alert("Please select at least one issue to add to the sprint");
    return false;
  }
  // Compile all information into an object to submit to the server
  let data = {
    source_repo_id: source_repo_id,
    sprint_name: sprint_name,
    issue_array: issue_array
  };

  // This method comes from django docs- it only sends the token if it is a post?
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
  }

  // Pull the token from the dom to include in the ajax call
  let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

  // Before the AJAX call, determine if the token is needed and add it to the header
  // if neccessary
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

  // Submit the info to the server with AJAX so that the page does not refresh
  $.ajax({
    method: "POST",
    url: "../createsprint/",
    data: data
  }).done(response => {
    saved_sprint = response.sprint_id;
    // After the server responds, open the modal
    $(".modal").toggleClass("is-active");
  });

  return false;
};

$(".hide_modal_button").click(e => {
  $(".modal").toggleClass("is-active");
  $("#confirm").attr("href", "");
});
