class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in range(len(operations)):
            operation = operations[i]
            if operation == '+':
                result.append(result[-1] + result[-2])
            elif operation == 'D':
                result.append(result[-1] * 2)
            elif operation == 'C':
                result.pop()
            else:
                result.append(int(operation))
        return sum(result)