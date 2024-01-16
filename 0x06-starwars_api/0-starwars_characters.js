#!/usr/bin/node
const request = require('request');
let content;
async function printName (i) {
  request(content[i], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (i < content.length - 1) {
        printName(i + 1);
      }
    }
  });
}
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    content = JSON.parse(body).characters;
    printName(0);
  }
});
