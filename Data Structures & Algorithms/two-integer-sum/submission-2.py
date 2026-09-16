#构造一个有序的、储存原始数字及其索引对应关系的列表，维护两个指针
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i,num in enumerate(nums):
            A.append([num,i])

        A.sort()
        i = 0
        j = len(nums) - 1
        cur = A[i][0]+A[j][0]
        while i < j:
            if cur == target:
                return [min(A[i][1],A[j][1]),max(A[i][1],A[j][1])]

            else:
                if cur < target:
                    i += 1
                else:
                    j -= 1

                cur = A[i][0]+A[j][0]
        return []


        