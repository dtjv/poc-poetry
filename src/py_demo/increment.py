def increment(num: int) -> int:
    return num + 1


def increment_by_step(num: int, step: int = 1) -> int:
    if step == 1:
        return increment(num)

    return num + step


def increment_all(nums: list[int]) -> list[int]:
    return [x + 1 for x in nums]
