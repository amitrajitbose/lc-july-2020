class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        dep = {}
        for i in range(numCourses):
            dep[i] = set([])
        for i,j in prerequisites:
            dep[i].add(j) # i dependent on j
        result = []
        visited, exploring = set([]), set([])
        def dfs(node):
            if node in visited:
                return
            exploring.add(node)
            for neighbor in dep[node]:
                if neighbor in exploring:
                    raise Exception('Cycle') # cycle founds
                if neighbor not in visited:
                    dfs(neighbor)
            exploring.remove(node)
            visited.add(node)
            result.append(node)
        for node in dep.keys():
            try:
                dfs(node)
            except Exception as e:
                return [] # loop exists
        return result

"""
Topo Sort (DFS)
O(V+E) Runtime
"""

