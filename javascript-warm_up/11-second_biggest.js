#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  console.log(args.sort((a, b) => b - a)[1]);
}
