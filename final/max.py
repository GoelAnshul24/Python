def lbs_to_kg(weight:float)->float:
    return weight * 0.45

def lbs_to_kg(weight:float)->float:
    return weight/0.45

def max_from_list(a)->int:
    max=a[0]
    for i in a:
        if (max<i):
            max=i
    return max