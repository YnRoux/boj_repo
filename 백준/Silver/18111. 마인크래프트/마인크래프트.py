import sys
from collections import Counter

def solve():
    input = sys.stdin.read().split()
    n = int(input[0])
    m = int(input[1])
    inventory = int(input[2])
    
    ground = list(map(int, input[3:]))
    height_counts = Counter(ground)
    
    min_time = float('inf')
    best_height = 0
    
    for target in range(257):
        needed_blocks = 0 
        removed_blocks = 0 
        
        for height, count in height_counts.items():
            if height > target:
                removed_blocks += (height - target) * count
            elif height < target:
                needed_blocks += (target - height) * count
        
        if removed_blocks + inventory >= needed_blocks:
            time = (removed_blocks * 2) + needed_blocks
            
            if time <= min_time:
                min_time = time
                best_height = target
                
    print(min_time, best_height)

solve()