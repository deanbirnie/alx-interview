#!/usr/bin/node

const request = require('request');

const getCharacters = (movieId) => {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(apiUrl, (error, response, body) => {
    if (error) throw error;

    const actors = JSON.parse(body).characters;
    displayCharactersInOrder(actors, 0);
  });
};

const displayCharactersInOrder = (actors, index) => {
  if (index === actors.length) return;

  request(actors[index], (error, response, body) => {
    if (error) throw error;

    const characterData = JSON.parse(body);
    console.log(characterData.name);

    displayCharactersInOrder(actors, index + 1);
  });
};

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command line argument.');
} else {
  getCharacters(movieId);
}
