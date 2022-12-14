#!/usr/bin/node
const request = require('request');

request.get(`${process.argv[2]}`, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  const dic = {};
  for (const task of JSON.parse(body)) {
    if (!(task.userId in dic) && task.completed) {
      dic[task.userId] = 1;
    } else if (!(task.userid in dic) && task.completed) {
      dic[task.userId]++;
    }
  }
  console.log(dic);
});
