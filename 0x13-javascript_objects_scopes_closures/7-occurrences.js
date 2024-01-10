#!/usr/bin/node
function nbOccurences (list, searchElement) {
  let count = 0;
  for (const item of list) {
    if (searchElement === item) {
      count++;
    }
  }
  return count;
}

module.exports = nbOccurences;
