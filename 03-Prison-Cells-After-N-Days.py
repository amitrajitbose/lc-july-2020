class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def transition( cells: List[int] ):
            next_state = [0] * 8
            for i in range(1, 7):
                if (cells[i - 1] + cells[i + 1]) in [0, 2]:
                    next_state[i] = 1 # occupied
                else:
                    next_state[i] = 0 # vacant
            return next_state
        
        # period of transition is 14 by observation
        N %= 14
        if N == 0:
            N = 14
        result = cells
        for i in range(N):
            result = transition(result)
            # print(result)
        return result

