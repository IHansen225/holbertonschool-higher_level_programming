#!/usr/bin/node
const request = require('request');

request.get(`${process.argv[2]}`, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  res_dict = {};
  for (task of JSON.parse(body)) {
    if (!(task.userId in res_dict) && task.completed) {
      res_dict[task.userId] = 1;
    } else if (!(task.userid in res_dict) && task.completed) {
      res_dict[task.userId]++;
    }
  }
  console.log(res_dict);
});
