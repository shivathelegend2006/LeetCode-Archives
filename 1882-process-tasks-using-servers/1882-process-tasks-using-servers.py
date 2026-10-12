import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        ans = []
        available = [(w,i) for i,w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        time = 0

        for j, task in enumerate(tasks):
            time = max(time,j) #sync the clock, either the task arrival time, ro current time

            if len(available) == 0:
                time = busy[0][0] #fast forwatrd when first server free

            while busy and busy[0][0] <= time:
                finsih, w, i = heapq.heappop(busy)
                heapq.heappush(available, (w,i))

            w,i = heapq.heappop(available)
            ans.append(i)
            heapq.heappush(busy, (time+ task, w, i))

        return ans
