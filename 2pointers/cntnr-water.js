/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
  const sortedHeights = [...height]
  sortedHeights.sort((a, b) => b-a)
  const uniqueHeights = new Set(sortedHeights)

  const iterator = uniqueHeights.entries();
  const max = iterator.next().value[0]
  const nextMax = iterator.next().value[0]

  const start = height.indexOf(max)
  const end = height.indexOf(nextMax)

  const diff = Math.abs(start - end)
  console.log(diff * nextMax)

    
};

// const height = [1,8,6,2,5,4,8,3,7]
const height = [1,1]
console.log(maxArea(height)) // 49