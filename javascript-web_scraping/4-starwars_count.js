#!/usr/bin/node
const request = require('request');

request.get(`${process.argv[2]}`, function(err, res, body) {
  if (err) {
    console.error(err);
  }
  let mcount = 0;

  for (movie of JSON.parse(body).results) {
    if (movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      mcount++;
    }
  }

  console.log(mcount);
});
