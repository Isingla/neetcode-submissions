class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scorecard = []
        for i in range(len(operations)):
            if operations[i] == '+':
                temp = scorecard[-1] + scorecard[-2]
                scorecard.append(temp)
            elif operations[i] == 'C':
                scorecard.pop(-1)
            elif operations[i] == 'D':
                scorecard.append(scorecard[-1]*2)
            else:
                scorecard.append(int(operations[i]))
        return sum(scorecard)