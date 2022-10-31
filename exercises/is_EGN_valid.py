def is_valid_UCN(ucn, should_bypass_checksum=False):
    if len(ucn) > 10 or len(ucn) < 10:
        return False

    if ucn[2] != 2:
        if ucn[2] != 4:
            if ucn[2] != 5:
                return False

    if ucn[2] == 5 and ucn[3] > 2:
        return False

    return True


print(is_valid_UCN('0146262382'))
