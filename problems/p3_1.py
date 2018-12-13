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


# f = open('../data/p3.data', 'r')
# data = f.readlines()
# f.close()
#
# claim_list = []
# count = 0
# for line in data:
#     claim_list.append(Claim(line))
#     count += 1
#     print(count)
# with open('../data/p3.pkl', 'wb') as f:
#     pickle.dump(claim_list, f)
# print("Processed")


with open('../data/p3.pkl', 'rb') as f:
    claim_list = pickle.load(f)
print("Loaded")

overlapping = 0
overlap_matrix = [[0 for x in range(1000)] for y in range(1000)]
for x in range(1000):
    print("Row: {}".format(x))
    for y in range(1000):
        found = False
        for claim in claim_list:
            if claim.matrix[x][y] == 1:
                if found:
                    overlapping += 1
                    overlap_matrix[x][y] = 1
                    break
                else:
                    found = True


print(overlapping)
# with open('../data/p3_p2.pkl', 'wb') as f:
#     pickle.dump(overlap_matrix, f)
# claim = Claim("#123 @ 3,2: 5x4")
# for row in claim.matrix:
#     print(row)
# i = 1
