#!/usr/bin/node
/*  Write a script that searches the second biggest integer in the list of arguments.
    You can assume all arguments can be converted to integer
    If no argument passed, print 0
    If the number of arguments is 1, print 0
    You must use console.log(...) to print all output
    You are not allowed to use var
*/
const args = process.argv.slice(2).map(x => parseInt(x));

if (args.length < 2) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => b - a);
  let second = sorted.find(n => n < sorted[0]);
  if (second === undefined) second = sorted[0];
  console.log(second);
}
