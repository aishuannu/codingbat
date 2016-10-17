def sum67(nums):
  sum = 0
  i = 0
  while i < len(nums):
    if nums[i] != 6:
      sum = sum + nums[i]
      i += 1
    else:
      i += (nums[i: ]. index(7)) + 1
  return sum
