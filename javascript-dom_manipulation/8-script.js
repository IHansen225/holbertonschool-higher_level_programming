fetch('https://stefanbohacek.com/hellosalut/?lang=fr')
  .then(response => response.json())
  .then(data => {
    const element = document.querySelector('#hello');
    element.innerHTML = data.hello;
  })
  .catch(error => console.log(error));