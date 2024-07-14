def rectangle_rotation(a, b):
    q = 2**0.5
    da = int(a / q + 1) 
    db = int(b / q + 1) 

    if int(a / q) % 2:
        za1, za2 = -1, 0
    else:
        za1, za2 = 0 , -1
        
    if int(b / q) % 2:
        zb1, zb2 = -1, 0
    else:
        zb1, zb2 = 0 , -1

    return (da + zb1) * (db +za1) + (da+zb2)*(db + za2) 