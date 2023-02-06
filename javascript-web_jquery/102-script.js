const $ = window.$;
$(document).ready(() => {
  $('input#btn_translate').click(() => {
    const value = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${value}`, (data) => $('DIV#hello').append(data.hello));
  });
});
