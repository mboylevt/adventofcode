import re
import pickle

class Claim():
    def __init__(self, line):
        id_re = r'#(\d+)\s'
        xyorig_re = r'(\d+),(\d+)'
        xylen_re = r'(\d+)x(\d+)'

        id_search = re.search(id_re, line)
        xyorig_search = re.search(xyorig_re, line)
        xylen_search = re.search(xylen_re, line)

        self.id = id_search.group(1)
        self.x_org = int(xyorig_search.group(1))
        self.y_org = int(xyorig_search.group(2))
        self.x_len = int(xylen_search.group(1))
        self.y_len = int(xylen_search.group(2))

        w = 1000
        h = 1000
        self.matrix = [[0 for x in range(w)] for y in range(h)]

        for x in range(self.y_org, self.y_org + self.y_len):
            for y in range(self.x_org, self.x_org + self.x_len):
                self.matrix[x][y] = 1



with open('../data/p3_p2.pkl', 'rb') as f:
    overlap_matrix = pickle.load(f)
print("Loaded overlap")
with open('../data/p3.pkl', 'rb') as f:
    claim_list = pickle.load(f)
print("Loaded claims")


for claim in claim_list:
    print("Claim {}".format(claim.id))
    ol = False
    for x in range(claim.y_org, claim.y_org + claim.y_len):
        if ol:
            break
        for y in range(claim.x_org, claim.x_org + claim.x_len):
            if overlap_matrix[x][y] == 1:
                ol = True
                break
    if not ol:
        print("No OL: {}".format(claim.id))
        break



# claim = Claim("#123 @ 3,2: 5x4")
# for row in claim.matrix:
#     print(row)
# i = 1
