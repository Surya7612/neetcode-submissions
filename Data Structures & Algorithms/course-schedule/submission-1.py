# from collections import defaultdict
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # Build the adjacency list(Directed Graph)
#         graph = defaultdict(list)


#         for course, prereq in prerequisites:
#             graph[course].append(prereq)
        
#         visited = set()

#         def dfs(course):
#             if course in visited:
#                 return False
#             if graph[course] == []:
#                 return True

#             visited.add(course)
#             for prereq in graph[course]:
#                 if not dfs(prereq):
#                     return False
            
#             visited.remove(course)
#             graph[course] = []
#             return True

#         for course in range(numCourses):
#             if not dfs(course):
#                 return False

#         return True

from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency graph and in_build array
        graph = defaultdict(list)
        # graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Initailize a queue with courses having no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        processed_courses = 0
        while queue:
            course = queue.popleft()
            processed_courses += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return processed_courses == numCourses