const $ = window.$;
const fetchedData = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
fetchedData.then((response) => {
  return response.json();
}).then((data) => {
  $('div#character').text(data.name);
});
