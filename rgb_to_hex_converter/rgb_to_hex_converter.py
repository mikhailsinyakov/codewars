def rgb_to_hex(r, g, b):
    # making sure that numbers are in the range 0-255
    values = [min(max(0, n), 255) for n in [r, g, b]]

    # convert each number to hex representation, drop 0x in the beginning
    # of the resulting string, convert that string to uppercase letters,
    # add zero in the beginning of the string, if the string contains only one
    # character, and join each of the resulting values into one string
    return "".join([hex(n)[2:].upper().zfill(2) for n in values])
