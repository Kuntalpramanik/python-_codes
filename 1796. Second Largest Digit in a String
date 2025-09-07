class Solution:
    def secondHighest(self, s: str) -> int:
        new_str=""
        for ch in s:
            if ch.isdigit():
                new_str+=ch
        array=[int(ch) for ch in new_str]
        if len(array)<2:
            return -1
        unique=list(set(array))
        if len(unique)<2:
            return -1        
        largest=second_largest=float('-inf')
        for num in unique:
            if num>largest:
                second_largest=largest
                largest=num
            elif num>second_largest:
                second_largest=num
        return second_largest
