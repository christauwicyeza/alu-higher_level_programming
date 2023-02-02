#!/usr/bin/node
const dict = require('./101-data.js').dict;
const result = {};

for (const prop in dict) {
  if (!Object.prototype.hasOwnProperty.call(result, dict[prop])) {
    result[dict[prop]] = [prop];
  } else {
    result[dict[prop]].push(prop);
  }
}
console.log(result);
