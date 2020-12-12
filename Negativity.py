def count_negatives(nums):

	negative_num=0
	for num in nums:
		if num<0:
  			negative_num=negative_num+1
	return negative_num
 
def count_negative(nums):
	return sum([num<0 for num in nums])

print(count_negative([1,-9,-3,-3]))
