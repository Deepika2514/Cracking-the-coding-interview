import collections

def isUnique(string):
    hm = collections.Counter(string)
    for elem in hm:
        if hm[elem] > 1:
            return False
    return True

if __name__ == "__main__":
    string = "abc"
    print(isUnique(string))
