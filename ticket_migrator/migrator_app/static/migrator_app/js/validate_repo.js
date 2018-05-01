// Check github for source repo before submitting to server

const check_github_for_source_repo = form => {
  const success = data => {
    if ("id" in data) {
      form.submit();
    } else {
      fail();
    }
  };

  const fail = (data = null) => {
    alert("Failed to validate source repo");
  };

  const url =
    "https://spyproxy.bangazon.com/student/commit/https://api.github.com/repos/" +
    form.source_repo.value.split("https://github.com/")[1];

  $.ajax({
    type: "GET",
    url: url
  }).then(success, fail);

  return false;
};
