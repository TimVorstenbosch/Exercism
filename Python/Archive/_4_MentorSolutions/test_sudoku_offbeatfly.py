def find_way(curr_size, goal, start, size, current, exclude):
    if goal == 0 and curr_size == size:
        return [current]
    elif curr_size == size:
        return []
    for num2 in range(start,10):
        if size ==  curr_size+1:
            diff = goal-num2
            if num2 in exclude or diff in exclude:
                continue
            elif diff > 9 or diff in current:
                continue
            elif diff == 0:
                return [current + [num2]]
            else:
                continue
        else:
            collect = find_way(curr_size+1,goal-num2,
                            num2+1, size,
                               current + [num2], exclude)
            if not collect:
                continue
            else:
                return collect

def combinations(target, size, exclude):
    options = []
    for num1 in range(1,10):
        if num1 in exclude:
            continue
        else:
            num1_options = find_way(1, target-num1, num1+1, 
                                    size, [num1], exclude)
            if num1_options:
                for option in num1_options:
                    options.append(option)
    return options

print( combinations( 10, 2, [1,4]) )