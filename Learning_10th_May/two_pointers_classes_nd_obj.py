class TwoPointerAlgorithm:
    def __init__(self, nums):
        self.nums = nums

    def find_pair_sum(self, target_sum):
        left = 0
        right = len(self.nums) - 1

        while left < right:
            current_sum = self.nums[left] + self.nums[right]

            if current_sum == target_sum:
                return [self.nums[left], self.nums[right]]
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
        return None

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10

two_pointer_algo = TwoPointerAlgorithm(nums)
result = two_pointer_algo.find_pair_sum(target_sum)

if result:
    print(f"Pair with sum {target_sum}: {result}")
else:
    print("No pair found.")
