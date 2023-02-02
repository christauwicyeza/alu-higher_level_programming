#!/usr/bin/node
const nbOccurences = function (list, searchElement) {
  return list.filter(el => el === searchElement).length;
};

exports.nbOccurences = nbOccurences;
