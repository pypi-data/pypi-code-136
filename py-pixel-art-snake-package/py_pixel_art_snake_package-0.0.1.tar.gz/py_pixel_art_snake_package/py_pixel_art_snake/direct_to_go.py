def direct_to_go(c1,actual_state):
    if(actual_state == 1):
        if (c1[0] > 0):
            return 1
        elif (c1[0] == 0):
            if (c1[1] <= 0):
                return 0
            else:
                return 2
        else:
            if (c1[1] <= 0):
                return 0
            else:
                return 2

    if(actual_state == 3):
        if (c1[0] < 0):
            return 3
        elif (c1[0] == 0):
            if (c1[1] <= 0):
                return 0
            else:
                return 2
        else:
            if (c1[1] <= 0):
                return 0
            else:
                return 2

    if(actual_state == 0):
        if (c1[1] < 0):
            return 0
        elif (c1[1] == 0):
            if (c1[0] >= 0):
                return 1
            else:
                return 3
        else:
            if (c1[0] >= 0):
                return 3
            else:
                return 1
    
    if(actual_state == 2):
        if (c1[1] > 0):
            return 2
        elif (c1[1] == 0):
            if (c1[0] >= 0):
                return 1
            else:
                return 3
        else:
            if (c1[0] >= 0):
                return 3
            else:
                return 1