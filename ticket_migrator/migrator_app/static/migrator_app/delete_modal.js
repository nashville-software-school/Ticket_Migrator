// Open the modal to confirm deletion and populate its text value based on the clicked element
$("._delete").click(e => {
  let sr_id = e.target.id;
  let sr_url = $(`.sr-${sr_id}`)[0].innerHTML;
  let href = $("#confirm").attr("href");
  $("#backlog_url")[0].innerHTML = sr_url;
  $(".modal").toggleClass("is-active");
  $("#confirm").attr("href", `${href}${sr_id}`);
});

// Close modal and remove the href for the confim button so you dont accidentally delete what you dont want
$(".hide_modal_button").click(e => {
  $(".modal").toggleClass("is-active");
  $("#confirm").attr("href", "");
});
