def isUnique(string):
    checker = 0
    for elem in string:
        val = ord(elem) - ord("a")
        if (checker & (1 << val)) > 0:
            return False
        checker = (checker | (1 << val))
    return True

if __name__ == "__main__":
    string = "abcdefd"
    print(isUnique(string))
