const test = arg => {
  const array = [];

  return Object.create(null, ({
    get: () => array,
    set: () => array.push(arg)
  }))
};

console.log(test(test))
console.log("1");