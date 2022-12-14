#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request.get(`${process.argv[2]}`, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  fs.writeFile(`${process.argv[3]}`, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }  
  });
});
