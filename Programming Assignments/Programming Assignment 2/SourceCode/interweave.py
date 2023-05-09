def helper_isinterweave(x, y, s, comps) -> tuple:
    """
    Dynamic program implementation which checks if a string s is interweave of strings x and y. Comps is a counter of
    operations
    :param x:string
    :param y:string
    :param s:string
    :param comps:int
    :return: tuple
    """
    # denote m and n the lengths of x and y respectively
    n, m = len(x), len(y)

    # create a table of results with dimmensions m+1 by n+1
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    # initialize the first row and column of the table with true
    dp[0][0] = True

    # state: dp[i][j] denote whether the first i+j letters in s is a
    # interleaving of the first i elements in x and the first j
    # elements in y
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] and (x[i - 1] == s[i - 1])
        comps += 1
    for i in range(1, m + 1):
        dp[0][i] = dp[0][i - 1] and (y[i - 1] == s[i - 1])
        comps += 1

    # state transition: matching last character in x and y with that
    # of s
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == s[i + j - 1]:  # s3[:3] = "abc", s1[2] = 'c'
                dp[i][j] = dp[i - 1][j]
                comps += 1
            if y[j - 1] == s[i + j - 1]:  # s3[:3] = "abc", s2[2] = 'c'
                dp[i][j] = dp[i][j] or dp[i][j - 1]
                comps += 1

    # result: whether entire s is an interleaving of entire x and y
    return dp[-1][-1], comps


def rec_isinterweave(x, y, s, comps) -> tuple:
    """
    Wrapper function that traverses the string s to see if it contains an interweave of strings x and y. This is a
    recursive version of isinterweave. Comps is an integer value used for counting operations
    :param x:
    :param y:
    :param s:
    :param comps:
    :return:
    """
    i = 0
    if len(s) < len(x) + len(y):
        return False, comps
    value, comps = helper_isinterweave(x, y, s, comps)
    if value:
        return True, comps
    else:
        return isinterweave(x, y, s[i + 1:], comps)


def isinterweave(x, y, s, comps):
    """
    Wrapper function that traverses the string s to see if it contains an interweave of strings x and y. Comps is an
    integer value used for counting operations
    :param x:
    :param y:
    :param s:
    :param comps:
    :return:
    """
    i = 0
    while len(s) - i >= len(x) + len(y):
        value, comps = helper_isinterweave(x, y, s[i:], comps)
        if value:
            return value, comps
        i += 1
    return False, comps
