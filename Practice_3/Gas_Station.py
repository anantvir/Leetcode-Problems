"""
Main Idea --> Iterate once over the gas array. Intialize 2 variables total_tank and curr_tank. For each item in gas
array, every time update total_tank = total_tank + (gas[i] - cost[i]) and curr_tank = curr_tank + (gas[i] - cost[i]).
Intuition for total tank is that we started with empty tank and then total tank went into negative numbers, we want to
see if we can recover the lost fuel which went into negatives. If at some point total_tank >= 0, then it means that
we have overall recovered the lost fuel. This approach requires O(n). Brute force requires checking all gas stations
as the starting point.
If at any point curr_tank < 0 , we assign the next gas station as the starting gas station, because the next station cannot
be reached from current station since curr_tank < 0
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        total_tank = 0
        curr_tank = 0
        start_idx = 0
        for i in range(n):
            total_tank = total_tank + (gas[i] - cost[i])
            curr_tank = curr_tank + (gas[i] - cost[i])
            if curr_tank < 0:                               # We cannot reach this station
                start_idx = i + 1
                curr_tank = 0                               # Start curr tank again, total tank remains the same
        return start_idx if total_tank >= 0 else -1