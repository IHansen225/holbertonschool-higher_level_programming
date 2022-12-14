#!/usr/bin/node
const request = require('request');

request.get(`https://swapi-api.hbtn.io/api/films/`, function(err, res, body) {
  let mcount = 0;

  for (movie of JSON.parse(body).results) {
    if (movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      mcount++;
    }
  }

  console.log(mcount);
});
