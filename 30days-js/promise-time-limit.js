/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
  return async function(...args) {
    new Promise((resolve, reject) => {
      resolve(fn.apply(this, args));
    
    }); // This is the time limit as a promise
  }
};

const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms


// const fun = (t) => new Promise(res => setTimeout(res, t));

// fun(100).then((v)=>console.log(v)).catch(console.log) // "Time Limit Exceeded" at t=100msx`