class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        prerequisites array is basically an adjacency matrix

        basically if there are are no cycles in our graph, 
        we should be able to finish all courses 

        BFS/DFS for a directed graph to detect if a cycle exists
        """
        adj_map = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj_map[course].append(prereq)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if adj_map[course] == []:
                return True

            visiting.add(course)
            for pre in adj_map[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            adj_map[course] = []
            return True

            
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True