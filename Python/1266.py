class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(points[i - 1][1] - points[i][1]), abs(points[i - 1][0] - points[i][0])) for i in range(1, len(points)))