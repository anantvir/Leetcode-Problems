class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict

        """---------------------- Make adjacency list stored in default dict ---------------------------"""
        adj_dict = defaultdict(list)
        for pair in prerequisites:
            next_course = pair[0]
            prev_course = pair[1]
            adj_dict[prev_course].append(next_course)
        
        visited = [False] * numCourses
        for currCourse in range(numCourses):
            if self.formsCycle(currCourse,adj_dict,visited):
                return False
        return True
    
    def formsCycle(self,currCourse,adj_dict,visited):
        if visited[currCourse]:
            return True
        visited[currCourse] = True
        return_val = False
        for neighbour in adj_dict[currCourse]:
            return_val = self.formsCycle(neighbour,adj_dict,visited)
            if return_val:
                break
        visited[currCourse] = False
        return return_val
        