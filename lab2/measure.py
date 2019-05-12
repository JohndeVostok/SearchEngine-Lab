label_dir = "data/ntcir14_test_label.txt"
res_dir = "vsmres.txt"
import math

if __name__ == "__main__":
    with open(label_dir, "r") as f:
        lines = f.readlines()
    rev = [{} for i in range(80)]
    for line in lines[1:]:
        tmp = line.strip().split()
        rev[int(tmp[0])-1][tmp[1]] = int(tmp[2])

    with open(res_dir, "r") as f:
        lines = f.readlines()
    res = [[] for i in range(80)]
    for line in lines:
        tmp = line.strip().split()
        res[int(tmp[0])-1].append(tmp[2])

    ts = [0, 0, 0]
    tc = [0, 0, 0]
    tk = [5, 10, 20]
    for i in range(80):
        bestrev = sorted([y for [x, y] in rev[i].items()], key=lambda x:-x)
        tmprev = []
        for s in res[i]:
            if s in rev[i]:
                tmprev.append(rev[i][s])
            else:
                tmprev.append(0)
        for j in range(3):
            k = tk[j]
            idcg = 0
            dcg = 0
            for t in range(k):
                idcg += (bestrev[t]) / math.log(j + 2, 2)
                dcg += (tmprev[t]) / math.log(j + 2, 2)
            if idcg != 0:
                ts[j] += dcg/idcg
                tc[j] += 1
    for i in range(3):
        print(ts[i]/tc[i])

