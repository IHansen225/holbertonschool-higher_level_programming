#!/usr/bin/node
const request = require('request');

request.get(`${process.argv[2]}`, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  let mcount = 0;

  for (const movie of JSON.parse(body).results) {
    for (const character of movie.characters) {
      if (character.endsWith('/18/')) {
        mcount++;
      }
    }
  }

  console.log(mcount);
});
