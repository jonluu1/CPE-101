def max_101(n1, n2):
    if n1 > n2:
        return n1
    if n2 > n1:
        return n2
    else:
        return False


def max_of_three(n1, n2, n3):
    constraint1 = max_101(n1, n2)
    if max_101 is False:
        return False
    else:
        return max_101(constraint1, n3)


def rental_late_fee(days):
    if days == 0:
        return 0
    if 0 < days <= 9:
        return 5
    if 9 < days <= 15:
        return 7
    if 15 < days <= 24:
        return 19
    if days > 24:
        return 100