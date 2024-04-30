var TimeLimitedCache = function() {
  this.cache = {}
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
  let ret = false;
  if (key in this.cache) {
    ret = true
  }
  this.cache = {
    [key]: value
  }
  setTimeout(()=> delete this.cache[key], duration)
  return ret;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
  if (key in this.cache) {
    return this.cache[key]
  }
  return -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.cache).length
};


const timeLimitedCache = new TimeLimitedCache()
console.log(timeLimitedCache.set(1, 42, 50)); // false
console.log(timeLimitedCache.set(1, 50, 100)); // false
console.log(timeLimitedCache.get(1)) // 42
console.log(timeLimitedCache.count()) // 1