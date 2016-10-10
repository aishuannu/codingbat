def sum13(nums):
  count = 0
  i = 0
  while i < len(nums):
    if nums[i] != 13:
      count = count + nums[i]
      i = i + 1
    else:
      i = i + 2
  return count

