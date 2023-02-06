const $ = window.$;
const fetchedData = fetch('https://fourtonfish.com/hellosalut/?lang=fr');
fetchedData.then((response) => {
  console.log(response.json());
  return response.json();
}).then((data) => {
  $('div#hello').append(data.hello);
});
