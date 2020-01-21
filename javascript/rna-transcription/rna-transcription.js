export const toRna = (dna) => {
  const DICTIONARY = {
    "G":"C",
    "C":"G",
    "T":"A",
    "A":"U",
  };

  return dna.split("").reduce((acc, val) => {
    return DICTIONARY[val] ? acc + DICTIONARY[val] : acc;
  }, '')

};
