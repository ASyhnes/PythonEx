def compute_closest_to_zero(ts):
    if not ts:
        return 0
    prochezero = ts[0]  

    for temp in ts:
        
        if abs(temp) < abs(prochezero) or (abs(temp) == abs(prochezero) and temp > prochezero):
            prochezero = temp  
    return prochezero
