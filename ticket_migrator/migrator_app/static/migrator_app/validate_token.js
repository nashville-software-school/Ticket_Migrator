// Check github for source repo before submitting to server

const check_token = form => {
  const token = form.token.value;

  if (token == "") {
    submit_form(form, true);
  } else {
    return validate_token(form, token);
  }
};

const submit_form = form => {
  form.submit();
};

const success = data => {
  if ("id" in data) {
    return true;
  } else {
    fail();
  }
};

const fail = (data = null) => {
  alert("Failed to validate Github PAC Token");
};

const validate_token = form => {
  const token = form.token.value;

  const url = "https://api.github.com/user";

  const headers = { Authorization: `token ${token}` };

  $.ajax({
    type: "GET",
    url: url,
    headers: headers
  })
    .then(success, fail)
    .then(x => {
      if (x) {
        submit_form(form);
      }
    });

  return false;
};
