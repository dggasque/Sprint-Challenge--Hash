def has_negatives(a):

    """
    YOUR CODE HERE
    """
    pos = {}
    neg = {}
    result = []
    for num in a:
        if num > 0:
            pos[num] = -num
        if num < 0:
            neg[num] = num * -1
    for key in pos:
        if pos[key] in neg:
            result.append(key)
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
