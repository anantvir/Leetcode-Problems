import heapq

class Solution(object):
    """--------------------------- Approach 1 (n*log(n)) ----------------------------"""
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key = lambda point:point[0]**2 + point[1]**2)                   # Sorting is atleast n*log(n)
        return points[:K]
    
    """------------------------- Approach 2 (Min Heap --> Overall Linear Time)--------------------------"""
    def kClosest2(self,points,K):
        distances = []
        for i in range(len(points)):                    # O(n)
            dist = points[i][0]**2 + points[i][1]**2
            distances.append((dist,points[i]))
        heapq.heapify(distances)                        # O(n)
        closest_points = []
        for i in range(K):
            closest_points.append(heapq.heappop(distances)[1])      # Remove element from heap takes O(log(n)) time !
        return closest_points


points = [[3,3],[5,-1],[-2,4]]
s = Solution()
print(s.kClosest2(points,2))
        