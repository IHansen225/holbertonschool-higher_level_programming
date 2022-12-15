fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const element = document.querySelector('#list_movies');
    for (const film of data.results) {
      const newLI = document.createElement('LI');
      const text = document.createTextNode(film.title);

      newLI.appendChild(text);
      element.appendChild(newLI);
    }
  })
  .catch(error => console.log(error));