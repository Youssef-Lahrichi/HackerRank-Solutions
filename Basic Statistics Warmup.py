import math
N = int(input())
nums = input().split()

for i in range(len(nums)):
    nums[i] = int(nums[i])

m = float(sum(nums)) / N
print(m)

sorted_arr = sorted(nums)
if N % 2 == 1:
    print(sorted_arr[math.floor(N/2)])
else:
    print(float((sorted_arr[math.floor(N/2-1)] + sorted_arr[math.floor(N/2)]) / 2))
    
mode = {}
for num in nums:
    if num in mode.keys():
        mode[num] += 1
    else:
        mode[num] = 1
mode_num = max(mode.values())

for num in sorted_arr:
    if mode[num] == mode_num:
        print(num)
        break

diff = 0
for num in nums:
    diff += (num - m)**2
std = round(math.sqrt(diff/N),1)
print(std)

ci_05 = round(m - 1.96*(std/math.sqrt(N)), 1)
ci_95 = round(m + 1.96*(std/math.sqrt(N)), 1)

print(ci_05, ci_95)
