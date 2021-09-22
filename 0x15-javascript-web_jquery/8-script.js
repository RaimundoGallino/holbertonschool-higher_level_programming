$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  data.results.forEach(element => {
    $('UL#list_movies').append(`<li>${element.title}</li>`);
  });
});
