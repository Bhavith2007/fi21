n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))
print(arr)  # Example: [10, 20, 30]
Sum_num = int(input("Enter the number Which you want to find pairs for: "))
pairs = [-1]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == Sum_num:
            pairs.append((arr[i], arr[j]))
if pairs == [-1]:
    print(f"No pairs found which sum to {Sum_num}")
else:
    pairs.remove(-1)
    print(f"The pairs which sum to {Sum_num} are: {pairs}")
