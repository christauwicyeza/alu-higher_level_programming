const $ = window.$;
$(document).ready(() => {
  $('input#btn_translate').click(() => {
    const value = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${value}`, (data) => $('DIV#hello').append(data.hello));
  });
  $('INPUT#language_code').keypress((event) => {
    if (event.which == 13) {
      $('input#btn_translate').click();
    }
  });
});
