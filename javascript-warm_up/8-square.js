#!/usr/bin/node

const arg = Number(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing size');
}
for (let i = 0; i < arg; i++) {
  console.log('X'.repeat(arg));
}
