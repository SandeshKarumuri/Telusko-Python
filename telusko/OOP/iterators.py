nums = [1, 2, 3, 4]
print(nums)
print()
print(nums[0])
print()
for i in nums:
    print(i)
print()
it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))
print()
for i in nums:
    print(i)