class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_freq = Counter(tasks)
        maxHeap = [-count for count in task_freq.values()]
        heapq.heapify(maxHeap) # most frequent task should be prioritized first
        
        q = deque() # cooldown for tasks
        time = 0

        while maxHeap or q: # tasks in both maxHeap and q exist

            time += 1
            if not maxHeap: # jump time forward to the next time a task becomes available
                time = q[0][1]

            else: 
                count = 1 + heapq.heappop(maxHeap) # this actually decrements the task amount
                if count:
                    q.append([count, time + n]) # append to cooldown [num of that task remaining, future time where it is valid to run]

            if q and q[0][1] == time: # task that was in cooldown is available to run
                heapq.heappush(maxHeap, q.popleft()[0]) # push the decremented task amount

        return time

