class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        INF = float('inf')

        # dp[1], dp[2], dp[3]
        dp = [INF, 1, 0, 1]

        for obs in obstacles:
            # Blocked lane
            if obs != 0:
                dp[obs] = INF

            # Update remaining lanes
            for lane in [1, 2, 3]:
                if lane != obs:
                    dp[lane] = min(
                        dp[lane],
                        1 + min(
                            dp[l] for l in [1, 2, 3]
                            if l != lane and l != obs
                        )
                    )

        return min(dp[1], dp[2], dp[3])