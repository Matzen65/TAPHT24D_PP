

def break_loop():
    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        #print(y)
        if x == end:
            break
    print(y)