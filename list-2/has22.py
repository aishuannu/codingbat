def has22(nums):
  if 2 in nums :
    for i in range(len(nums)):
      if nums[i : i + 2] == [2, 2]:
        return True
  return False

