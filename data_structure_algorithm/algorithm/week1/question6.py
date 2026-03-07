# find minimum value between three vrariables
def min_of_three(a, b, c):
    minimum = a
    if b < minimum:
        minimum = b
    if c < minimum:
        minimum = c
    return minimum
