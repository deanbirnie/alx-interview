#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + movieId + '/';

request(url, function (error, response, body) {
  if (error) throw error;
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (error, response, body) {
      if (error) throw error;
      console.log(JSON.parse(body).name);
    });
  }
});
