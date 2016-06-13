def kmp_search(text, pattern):
    """
    An implementation of Knuth-Morris-Patt substring search algorithm
    KMP accesses no more than M+N characters to search for a pattern of length M in a text of length N
    @param text: the text to be search from
    @param pattern: the pattern to be search for
    @return: the index of the first occurrence of the pattern in text
    """
    def construct_dfa(txt, pat):
        """
        Proportional to R*M where R is the # characters in text, M is the length of pattern
        @param text: the text to be search from
        @param pattern: the pattern to be search for
        @return: return the dfa table
        """
        characters = list(set(txt))
        r = len(characters)
        m = len(pat)
        dfa = dict()  # dfa table
        dfa[pat[0]] = [0 for j in range(0, m)]
        dfa[pat[0]][0] = 1
        x = 0  # current state
        for i in range(1, m):
            for c in characters:
                if c not in dfa.keys():
                    dfa[c] = [0 for k in range(0, m)]
                dfa[c][i] = dfa[c][x]  # copy over

            dfa[pat[i]][i] = i + 1  # update next state
            x = dfa[pat[i]][x]  # update current state

        return dfa

    dfa = construct_dfa(text, pattern)
    j = 0  # current state
    m = len(pattern)
    n = len(text)
    i = 0
    while i < n and j < len(pattern):
        j = dfa[text[i]][j]
        i += 1

    if j == m:
        return i - m
    else:
        return -1


def boyer_moore_search(text, pattern):
    def build_right(txt, pat):
        characters = list(set(txt))
        r = len(characters)
        m = len(pat)
        right = dict()
        for c in characters:
            right[c] = -1
        for c in range(0, m):
            right[pattern[c]] = c
        return right

    right = build_right(text, pattern)
    m = len(pattern)
    n = len(text)
    i = 0

    while i <= n - m:
        skip = 0

        for j in range(m - 1, -1, -1):
            c = text[i+j]
            if pattern[j] != c:
                # calculate skip
                skip = max(1, j - right[c])
                break

        if skip == 0:
            return i

        i += skip

    return -1


def rabin_karp_search(text, pattern, q=5):
    """
    An implementation of Rabin Karp search
    @param text:
    @param pattern:
    @param q:
    @return:
    """
    def hash(key, m, r, q):
        h = 0
        for j in range(0, m):
            h = (r * h + int(ord(key[j]))) % q
        return h

    r = 256
    m = len(pattern)

    # precompute r^(m-1) mod Q
    rm = 1
    for i in range(1, m):
        rm = (r * rm) % q

    pat_hash = hash(pattern, m, r, q)
    txt_hash = hash(text, m, r, q)
    n = len(text)
    if txt_hash == pat_hash:
        return 0

    i = m
    while i < n:
        txt_hash = (txt_hash + q - rm * int(ord(text[i-m]))) % q
        txt_hash = (txt_hash * r + int(ord(text[i]))) % q
        if txt_hash == pat_hash:
            return i - m + 1
        i += 1

    return -1

if __name__ == "__main__":
    print rabin_karp_search("123456789", "456")