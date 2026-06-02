from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        best_time = float("inf")
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land_finish_time = landStartTime[i] + landDuration[i]
                water_start_time = max(waterStartTime[j], land_finish_time)
                water_finish_time = water_start_time + waterDuration[j]
                best_time = min(best_time, water_finish_time)

                water_finish_time_2 = waterStartTime[j] + waterDuration[j]
                land_start_time_2 = max(landStartTime[i], water_finish_time_2)
                land_finish_time_2 = land_start_time_2 + landDuration[i]
                best_time = min(best_time, land_finish_time_2)
        return best_time
        