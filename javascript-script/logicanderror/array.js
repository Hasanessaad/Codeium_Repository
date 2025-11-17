function removeDuplicates(arr) {
  return arr.filter((el, i, arr) => arr.indexOf(el) === i); // just a smiple comment
}
