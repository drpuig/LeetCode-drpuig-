class Solution:
    def backtracking(self, answer, mapNumberLetter, digits, combination, index):
        if(index > len(digits)):
            return
        if(len(combination) == len(digits)):
            answer.append(combination[:])
            return
        currentDigit = digits[index]
        curString = mapNumberLetter[currentDigit]
        for i in range(len(curString)):
            self.backtracking(answer, mapNumberLetter, digits, combination + curString[i], index + 1)
    
    
    
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits) == 0):
            return []
        answer = []
        mapNumberLetter = {}
        mapNumberLetter['2'] = "abc"
        mapNumberLetter['3'] = "def"
        mapNumberLetter['4'] = "ghi"
        mapNumberLetter['5'] = "jkl"
        mapNumberLetter['6'] = "mno"
        mapNumberLetter['7'] = "pqrs"
        mapNumberLetter['8'] = "tuv"
        mapNumberLetter['9'] = "wxyz"
        
        self.backtracking(answer, mapNumberLetter, digits, "", 0)
        return answer
        
        