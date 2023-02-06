const $ = window.$;
const fetchedData = fetch('https://swapi-api.hbtn.io/api/films/?format=json');
fetchedData.then((response) => {
  return response.json();
}).then((data) => {
  data.results.forEach(el => {
    $('ul#list_movies').append(`<li>${el.title}</li>`);
  });
//
});
