# https://leetcode.com/problems/search-in-rotated-sorted-array

def search(nums, target)
  nums.each_with_index do |ele, indx|
    return indx if ele == target
  end
  return -1
end
