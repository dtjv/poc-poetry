def increment(num):
    return num + 1


def increment_by_step(num, step=1):
    if step == 1:
        return increment(num)

    return num + step
