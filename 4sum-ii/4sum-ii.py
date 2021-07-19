class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash_table = {}
        answer = 0
        for i in range(0, len(nums1)):
            x = nums1[i]
            for j in range(0, len(nums2)):
                y = nums2[j]
                if x + y not in hash_table:
                    hash_table[x + y] = 0
                hash_table[x + y] += 1
        for i in range(0, len(nums3)):
            x = nums3[i]
            for j in range(0, len(nums4)):
                y = nums4[j]
                target = -(x + y)
                if target in hash_table:
                    answer += hash_table[target]
        return answer
        