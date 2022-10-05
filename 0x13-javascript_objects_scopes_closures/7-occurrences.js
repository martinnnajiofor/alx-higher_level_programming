#!/usr/bin/node
/*Write a function that returns the number of occurrences in a list:

Prototype: exports.nbOccurences = function (list, searchElement)
*/
exports.nbOccurences = function (list, searchElement) {
  let idx = list.indexOf(searchElement);
  let nb = 0;
  while (idx !== -1) {
    nb++;
    idx = list.indexOf(searchElement, ++idx);
  }
  return nb;
};
