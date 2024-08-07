$(document).ready(function () {
  function fetchTranslation() {
    var languageCode = $("#language_code").val();
    var url =
      "https://www.fourtonfish.com/hellosalut/hello/?lang=" + languageCode;
    $.get(url, function (data) {
      $("#hello").text(data.hello);
    }).fail(function () {
      $("#hello").text("Error: Unable to fetch translation");
    });
  }
  $("#btn_translate").click(function () {
    fetchTranslation();
  });
  $("#language_code").keyup(function (event) {
    if (event.key === "Enter") {
      fetchTranslation();
    }
  });
});
