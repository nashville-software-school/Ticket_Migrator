// Check github for source repo before submitting to server

const check_github_for_source_repo = form => {
  const success = data => {
    form.submit();
  };

  const fail = data => {
    alert("Source Repo Not Valid");
  };

  const url =
    "https://api.github.com/repos/" +
    form.source_repo.value.split("https://github.com/")[1];
  let authToken;
  let headers;
  if ((authToken = JSON.parse(localStorage.getItem("Authorization")))) {
    headers = { Authorization: "token " + authToken };
  }

  $.ajax({
    type: "GET",
    url: url,
    headers: headers
  }).then(success, fail);

  return false;
};
