def solution(nums):
    pick = len(nums) // 2
    species = len(set(nums))
    return min(pick, species)