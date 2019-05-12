import json

doc_dir = "data/ntcir14_test_doc.json"
query_dir = "data/ntcir14_test_query.json"
idf_dir = "data/term_idf.txt"


def load_doc(idf, docs_tf, docs_id, docs_len):
    with open(doc_dir, "r") as f:
        lines = f.readlines()
        for line in lines:
            doc_tf = {}
            ll = 0
            tmp = json.loads(line.strip())
            for term in tmp["content_seg"].split():
                if not term in doc_tf:
                    doc_tf[term] = 0
                doc_tf[term] += 1
                ll += 1
            docs_tf.append(doc_tf)
            docs_id.append(tmp["uid"])
            docs_len.append(ll)
            tmp = 0
            for term in doc_tf:
                if not term in idf:
                    continue
                tmp += (idf[term] * doc_tf[term]) ** 2
            docs_mod.append(tmp ** 0.5)


def load_idf(idf):
    with open(idf_dir, "r") as f:
        lines = f.readlines()
        for line in lines:
            tmp = line.strip().split()
            idf[tmp[0]] = float(tmp[1])


def load_query(query):
    with open(query_dir, "r") as f:
        lines = f.readlines()
        for line in lines:
            query.append(json.loads(line.strip()))


if __name__ == "__main__":
    idf = {}
    load_idf(idf)
    docs_tf = []
    docs_id = []
    docs_mod = []
    docs_len = []
    load_doc(idf, docs_tf, docs_id, docs_len)
    queries = []
    load_query(queries)
    doc_num = len(docs_tf)

    k1 = 2
    k2 = 1
    b = 0.75

    dlsum = 0
    for l in docs_len:
        dlsum += l
    dlavg = dlsum / doc_num

    res = []
    qid = 0
    for query in queries:
        qid += 1
        q_terms = query["query_seg"].split()
        scores = []
        for i in range(doc_num):
            k = k1 * (1 - b + b * docs_len[i] / dlavg)
            score = 0
            for term in q_terms:
                if term in docs_tf[i]:
                    score += idf[term] * docs_tf[i][term] * (k1 + 1) / (docs_tf[i][term] + k)
            scores.append([i, score])
        s = sorted(scores, key=lambda x:-x[1])
        for i in range(20):
            res.append([str(qid), "Q0", docs_id[s[i][0]], str(i + 1), str(s[i][1]), "bm25"])
    with open("bm25res.txt", "w") as f:
        lines = []
        for tmp in res:
            lines.append(" ".join(tmp) + "\n")
        f.writelines(lines)

