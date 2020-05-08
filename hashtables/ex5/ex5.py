import os

def finder(files, queries):

    """
    YOUR CODE HERE
    """
    dic = {}
    q = {}
    result = []
    for query in queries:
        q[query] = []
    for f in files:
        dic[f] = os.path.basename(f)
    for key in dic:
        if dic[key] in q:
            result.append(key)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
