def collision(c1, c2):

    c3 = c1[0] - c2[0]
    c4 = c1[1] - c2[1]
    
    return (abs(c3) < 10.0) and (abs(c4) < 10.0)