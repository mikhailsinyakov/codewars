def solution(nums):
    nums_with_ranges = []

    num1 = None
    num2 = None

    # added element to a list as a way to not repeat a block of code in else statement
    for cur_num in nums + [float("inf")]:
        if num1 is None:
            num1 = cur_num
        elif (num2 is not None and cur_num == num2 + 1) or cur_num == num1 + 1:
            num2 = cur_num
        else:
            if num2 is not None and num2 - num1 > 1:
                nums_with_ranges.append(f"{num1}-{num2}")
            else:
                nums_with_ranges.append(str(num1))
                if num2 is not None:
                    nums_with_ranges.append(str(num2))

            num1 = cur_num
            num2 = None

    return ",".join(nums_with_ranges)
