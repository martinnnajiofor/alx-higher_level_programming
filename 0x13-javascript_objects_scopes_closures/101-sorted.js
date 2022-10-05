#!/usr/bin/node
/*Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

Your script must import dict from the file 101-data.js
In the new dictionary:
A key is a number of occurrences
A value is the list of user ids
Print the new dictionary at the end
*/
const Dict = require('./101-data').dict;
const Res = {};
for (const key in Dict) {
  if (!Res[Dict[key]]) {
    Res[Dict[key]] = [];
  }
  Res[Dict[key]].push(key);
}
console.log(Res);
