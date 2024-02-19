def solution(sizes):
    max_w, max_h = 0, 0
    
    for size in sizes:
        w, h = size
        
        if w >= h:
            max_w = max(max_w, w)
            max_h = max(max_h, h)
        
        else:
            max_w = max(max_w, h)
            max_h = max(max_h, w)
        
    answer = max_w * max_h

    return answer