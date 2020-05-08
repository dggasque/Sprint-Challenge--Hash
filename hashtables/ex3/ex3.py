def intersection(arrays):

    """
    YOUR CODE HERE
    """
    dic = {}
    result = []
    
    for num in arrays[0]:
        dic[num] = 1
    
    for array in arrays[1:]:
        for num in array:
            if num in dic:
                dic[num] += 1
    
    for key in dic:
        if dic[key] == len(arrays):
            result.append(key)
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
