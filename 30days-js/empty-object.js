var isEmpty = function(arg) {
  //check if arg is an object or array
  if (typeof arg === 'object') { 
    return Object.keys(arg).length === 0;
  } else if (typeof arg === 'array') {
    return arg.length === 0;
  }
};