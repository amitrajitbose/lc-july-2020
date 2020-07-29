from heapq import heappush, heappop
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time, heap = 0, []
        for k,v in Counter(tasks).items():
            heappush(heap, (-1*v, k)) # maxHeap: thus negate into minheap
        while len(heap):
            i, temp = 0, []
            while i < (n + 1):
                time += 1
                if heap:
                    k, v = heappop(heap)
                    if k != -1:
                        temp.append((k+1, v)) # plus one because one task instance is going to be done
                if not heap and not temp:
                    break # all tasks done
                else:
                    i += 1
            # once cycle is done, now push the elements in temp list again and process again
            for item in temp:
                heappush(heap, item)
        return time

##############################
# Runtime : O(len(tasks) * n)#
# Space : O(26) ~= O(1)      #
# Company Tags: Facebook     #
##############################

