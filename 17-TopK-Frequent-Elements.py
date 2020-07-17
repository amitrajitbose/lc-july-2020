"""
Facebook Interview Problem
**************************
"""

from heapq import heappush, heappushpop
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.topKFrequentCounter(nums, k)
    
    def topKFrequentBuckets_Jeet(self, nums: List[int], k: int) -> List[int]:
        count = [set([]) for i in range(len(nums)+1)] # map of buckets
        freq = Counter(nums)
        for i in set(nums):
            count[freq[i]].add(i)

        res = []
        for i in range(len(nums), 0, -1):
            if len(res) >= k:
                return res[:k]
            
            if len(count[i]) > 0:
                res.extend(list(count[i]))
        return res
    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        """
        Max heap approach
        
        k = k most frequent elements
        
        Time complexity:  O(n log k)
        Space complexity: O(n)
        """
        maxheap = []

        for num, freq in Counter(nums).items():
            if len(maxheap) == k:
                heappushpop(maxheap, (freq, num))
            else:
                heappush(maxheap, (freq, num))
        # print(maxheap)
        return [x[1] for x in maxheap]
            
    def topKFrequentCounter(self, nums: List[int], k: int) -> List[int]:
        """
        Counter (Dictionary) approach
        
        n = unique integers
        
        Time complexity:  O(n log n)
        Space complexity: O(n)
        """
        return [x[0] for x in Counter(nums).most_common(k)]
        
    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        """
        Bucket sort approach
        
        Time complexity:  O(n)
        Space complexity: O(n)
        """
        buckets = [[] for _ in nums]
        for num, freq in Counter(nums).items():
            buckets[-freq].append(num)
        return list(itertools.chain(*buckets))[:k]


