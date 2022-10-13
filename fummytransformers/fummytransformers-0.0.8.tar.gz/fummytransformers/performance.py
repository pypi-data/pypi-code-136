import multiprocessing as mp


def f_vs_files(f, fns):
    workers = mp.cpu_count()
    with mp.Pool(workers) as p:
        p.map(f, fns)


def nlp_stanza(text):
    nlp = stanza.Pipeline("fr", logging_level='WARN', use_gpu=False)
    doc = nlp(text)
    for sent in doc.sentences:
        with open(text+".txt", 'w') as f:
            f.write(sent.text)


def nlp_stanza2(nlp, text):
    doc = nlp(text)
    for sent in doc.sentences:
        with open(text+".txt", 'w') as f:
            f.write(sent.text)


if __name__ == "__main__":
    import stanza
    from itertools import repeat
    nlp = stanza.Pipeline("fr", logging_level='WARN', use_gpu=False)
    texts = ["la dd", "je suis beau"]
    # f_vs_files(nlp_stanza2, zip(repeat(nlp),texts))
    workers = mp.cpu_count()
    with mp.Pool(workers) as p:
        p.starmap(nlp_stanza2, zip(repeat(nlp), texts))
