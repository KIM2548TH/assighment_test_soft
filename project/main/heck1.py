

def funnyString(s):
    original_diff = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1)]

    reversed_diff = [abs(ord(s[::-1][i]) - ord(s[::-1][i+1])) for i in range(len(s)-1)]
    
    if original_diff == reversed_diff:
        return "Funny"
    else:
        return "Not Funny"
    