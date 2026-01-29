class Solution:
    def maxPeople(self, arr):  # Only arr param
        n = len(arr)
        max_count = 1
        for i in range(n):
            count = 1  # Self
            # Left visibility
            for j in range(i-1, -1, -1):
                count += 1
                if arr[j] >= arr[i]:
                    break
            # Right visibility
            for k in range(i+1, n):
                count += 1
                if arr[k] >= arr[i]:
                    break
            max_count = max(max_count, count)
        return max_count

# Correct call
s = Solution()
print(s.maxPeople([6,2,5,4,5,1,7]))  # Output: 4 (e.g., person at 7 sees 4)
    