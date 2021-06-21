def arrange(s):
    t = []
    left_index, right_index = 0, len(s) - 1
    first_select_left = True

    while left_index < right_index:
        left_value = s[left_index]
        right_value = s[right_index]
        t.append(left_value if first_select_left else right_value)
        t.append(right_value if first_select_left else left_value)

        left_index += 1
        right_index -= 1
        first_select_left = not first_select_left

    if len(s) % 2 == 1:
        middle_value = s[len(s)//2]
        t.append(middle_value)

    return t
