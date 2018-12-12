import difflib


def get_diff(orig, comp):
    matches = difflib.SequenceMatcher(None, orig, comp).get_matching_blocks()
    final = ''
    for match in matches:
        final = final + orig[match.a:match.a + match.size]
    return final

f = open('../data/p2.data', 'r')
data = f.readlines()
f.close()

for orig in data:
    for comp in data:
        if orig == comp:
            continue
        final = get_diff(orig, comp)
        if len(final)+ 1 == len(orig):
            print(final)