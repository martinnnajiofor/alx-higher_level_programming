#!/usr/bin/node
/*Write a function that returns the reversed version of a list:

Prototype: exports.esrever = function (list)
You are not allow to use the built-in method reverse
*/
exports.esrever = function (list) {
  const ListRev = [];
  for (let idx = list.length - 1; idx >= 0; idx--) {
    ListRev.push(list[idx]);
  }
  return ListRev;
};
