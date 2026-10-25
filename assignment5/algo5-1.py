##Input: s1 = "ab", s2 = "eidbaooo"

##Output: true

##Input: s1 = "ab", s2 = "eidboaoo"

##Output: false

def Backtracking(s1, s2):
    if len(s1) > len(s2):
        return False
        
    chars = list(s1)
    found = False

    def backtrack(first):
        nonlocal found
        if found:
            return
        
        if first == len(chars):
            permutation = "".join(chars)
            if permutation in s2:
                found = True
            return
            
        for i in range(first, len(chars)):
            chars[first], chars[i] = chars[i], chars[first]

            backtrack(first + 1)

            chars[first], chars[i] = chars[i], chars[first]

    backtrack(0)
    return found

s1 = "ab"
s2 = "eidbaooo"
print(Backtracking(s1, s2))