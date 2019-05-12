import json

doc_dir = "data/ntcir14_test_doc.json"
query_dir = "data/ntcir14_test_query.json"
idf_dir = "data/term_idf.txt"


def load_doc(idf, docs_tf, docs_id):
    with open(doc_dir, "r") as f:
        lines = f.readlines()
        for line in lines:
            doc_tf = {}
            tmp = json.loads(line.strip())
            for term in tmp["content_seg"].split():
                if not term in doc_tf:
                    doc_tf[term] = 0
                doc_tf[term] += 1
            docs_tf.append(doc_tf)
            docs_id.append(tmp["uid"])
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
    load_doc(idf, docs_tf, docs_id)
    queries = []
    load_query(queries)
    doc_num = len(docs_tf)

    res = []
    qid = 0
    for query in queries:
        qid += 1
        q_terms = query["query_seg"].split()
        scores = []
        qw = 0
        for term in q_terms:
            qw += idf[term] ** 2
        qw = qw ** 0.5
        for i in range(doc_num):
            score = 0
            for term in q_terms:
                if term in docs_tf[i]:
                    score += idf[term] * idf[term] * docs_tf[i][term]
            score /= docs_mod[i] * qw
            scores.append([i, score])
        s = sorted(scores, key=lambda x:-x[1])
        for i in range(20):
            res.append([str(qid), "Q0", docs_id[s[i][0]], str(i + 1), str(s[i][1]), "vsm"])
    with open("vsmres.txt", "w") as f:
        lines = []
        for tmp in res:
            lines.append(" ".join(tmp) + "\n")
        f.writelines(lines)



