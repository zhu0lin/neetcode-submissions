class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Understand
        Input: An integer target which represents the destination all
        cars are traveling to. 
        An array position where position[i] represents the position of the ith car. 
        An array speed where speed[i] represents the speed of the ith car.
        Output: An integer that represents the number of different
        car fleets that will arrive at the destination.

        Plan

        """
        position_speed = []
        for i in range(len(position)):
            position_speed.append([position[i], speed[i]])
        position_speed.sort(reverse=True)

        stack = []
        for i in range(len(position_speed)):
            time = (target - position_speed[i][0]) / position_speed[i][1]
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
