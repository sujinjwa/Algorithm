string = input()

# 첫번째 방법
# arr = list(string)
# arr.sort()
# sorted_str = ''.join(arr)

# print(sorted_str)

# 두번째 방법
arr = sorted(string)
sorted_str = ''.join(arr)

print(sorted_str)