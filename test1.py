def identify_longest_shared_start(words):
    
    if not words:
        return ""

    
    shortest_word = min(words, key=len)
    
    
    for i, character in enumerate(shortest_word):
        
        for word in words:
            
            if word[i] != character:
                return shortest_word[:i]
    
    return shortest_word

words1 = ["light", "live", "liver"]
print(identify_longest_shared_start(words1)) # Result: "li"

words2 = ["light", "racecar", "car"]
print(identify_longest_shared_start(words2)) # Result: ""

