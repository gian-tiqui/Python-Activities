class Solution(object):
    @staticmethod
    def remove_duplicates(self, nums):
        d = dict()

        for i in nums:
            if i in d.keys():
                d[i] = d[i] + 1
            else:
                d[i] = 1

        nums.clear()

        for i in d.keys():
            nums.append(i)
            