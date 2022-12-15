fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    const element = document.querySelector('#character');
    element.innerHTML = `<ul><li>${data.name}</li></ul>`;
  })
  .catch(error => console.log(error));