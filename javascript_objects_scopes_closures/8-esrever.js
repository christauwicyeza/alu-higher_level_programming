#!/usr/bin/node
const esrever = function (list) {
  const reverseArrr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverseArrr.push(list[i]);
  }
  return reverseArrr;
};

exports.esrever = esrever;
