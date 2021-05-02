def average(num):
    sum = 0
    for t in num:
        if isinstance(t, int):
            sum += int(t)

    return sum / len(num)

# I consulted https://www.guru99.com/find-average-list-python.html as I am unfamiliar with python lists
# I believe my code is sufficiently unique to to shortenings I made plus the value checking to not be plagiarism