from collections import deque


def is_match_possible(candidate, test_word):
    """
    Check if some letters can be replaced with hyphens
    in the candidate word so that it can be converted to 
    the test word by removing these hyphens
    """
    i, j = 0, 0  # i - candidate index, j - test_word index

    # we need to make sure that the candidate word contains
    # all the letters that the test word contains, in the same order
    # there may be other letters or symbols in between these letters
    while j < len(test_word):
        if i >= len(candidate):
            return False
        if candidate[i] == test_word[j]:
            j += 1
        i += 1

    return True


def get_possible_candidates(candidate):
    """
        Get a list of strings you can get by replacing 
        every non-hyphen symbol with a hyphen
    """
    no_hyphen_idx = [i for i, sym in enumerate(candidate) if sym != "-"]
    new_candidates = [
        f"{candidate[:i]}-{candidate[i+1:]}" for i in no_hyphen_idx]

    return new_candidates


def bananas(string):
    test_word = "banana"
    exp_hyphen_count = len(string) - len(test_word)

    q = deque()
    q.append(string)
    matches = set()

    while q:
        candidate = q.pop()
        if is_match_possible(candidate, test_word):
            if candidate.count("-") == exp_hyphen_count:
                matches.add(candidate)
            else:
                for next_candidate in get_possible_candidates(candidate):
                    q.append(next_candidate)

    return matches

# This algorithm seems to be correct, but I got an Execution Timeout error.


if __name__ == "__main__":
    print(bananas("bananaananaaaa"))
