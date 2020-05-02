def lines(a, b):
    """Return lines in both a and b"""

    lines_O_a = a.split('\n')
    lines_O_b = b.split('\n')

    lines_O_a = set(lines_O_a)
    lines_O_b = set(lines_O_b)
    common_lines = lines_O_a.intersection(lines_O_b)

    return list(common_lines)


def sentences(a, b):
    """Return sentences in both a and b"""

    from nltk.tokenize import sent_tokenize

    sentences_O_a = sent_tokenize(a)
    sentences_O_b = sent_tokenize(b)

    sentences_O_a = set(sentences_O_a)
    sentences_O_b = set(sentences_O_b)
    common_sentences = sentences_O_a.intersection(sentences_O_b)

    return list(common_sentences)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    substrings_O_a = [a[i:i+n] for i in range(len(a)-n+1)]
    substrings_O_b = [b[j:j+n] for j in range(len(b)-n+1)]

    common_substrings = []
    if len(substrings_O_a) < len(substrings_O_b):
        for substring in substrings_O_a:
            if substring in substrings_O_b:
                common_substrings.append(substring)
    else:
        for substring in substrings_O_b:
            if substring in substrings_O_a:
                common_substrings.append(substring)

    common_substrings = set(common_substrings)

    return list(common_substrings)
