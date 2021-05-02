def average(num):
    sum = 0
    for t in num:
        if (t.is_numeric()):
            sum += int(t)

    return sum / len(num)