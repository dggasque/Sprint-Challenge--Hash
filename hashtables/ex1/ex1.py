def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    dic = {}
    for i, x in enumerate(weights):
        if x in dic:
            dic[x] = dic[x] + [i]
        else:
            dic[x] = [i]   
    for key1 in dic:
        key2 = limit - key1 
        if len(dic[key1]) > 1:
            if key1 * 2 == limit:
                return (dic[key1][1], dic[key1][0])
        if key2 in dic:
            if key1 != key2:
                index1 = dic[key1][0]
                index2 = dic[key2][0]
                if index1 < index2:
                    return (index2, index1)
                if index2 < index1:
                    return (index1, index2)
    return None
