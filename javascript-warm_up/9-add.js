#!/usr/bin/node
const { argv } = process;

function add (a, b) {
  console.log(a + b);
}

add(parseInt(argv[2]), parseInt(argv[3]));
