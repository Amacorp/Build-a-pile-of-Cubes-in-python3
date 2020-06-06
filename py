def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1
    
    
or


def find_nb(m):
    try:
        vol = int(m)
    except TypeError:
        return -1
    
    partial_sum = 0
    i = 0
    while partial_sum < vol:
        i += 1
        partial_sum += i**3
    
    if vol == partial_sum:
        return i
    else:
        return -1
        
        
or


def find_nb(m):
    a = int((2*m**0.5)**0.5)
    if (a*(a+1)/2)**2 == m:
        return a
    return -1
