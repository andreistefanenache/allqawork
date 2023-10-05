"""This is the counter module, it counts things"""
def count(sequence, item):
    """This counts the number of item in sequence"""
    y = 0
    for n in sequence:
        if n == item:
            y += 1
    return y
