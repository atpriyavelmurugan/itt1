nums = list(eval(input("Enter the list: ")))
val = int(input("Enter the number: "))
l1=len(nums);
k = 0
# Logic: We only need to copy non-val elements to the front
for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1
for i in range(k,l1):
   nums[i]='_';

print(f"k = {k}")
print(f"Modified list: {nums}")
