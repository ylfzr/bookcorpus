import os
import sys
from glob import glob

from nltk.tokenize import sent_tokenize

file_dir = sys.argv[1]


def convert_into_sentences(lines):
    blank = 0
    stack = []
    sent_L = []
    n_sent = 0
    for chunk in lines:
        if not chunk.strip():
            blank += 1
            if blank >= 2:
                if stack:
                    sents = sent_tokenize(
                        " ".join(stack).strip().replace('\n', ' '))
                    sent_L.extend(sents)
                    n_sent += len(sents)
                    sent_L.append('\n')
                    stack = []
                blank = 0
            continue
        stack.append(chunk.strip())

    if stack:
        sents = sent_tokenize(" ".join(stack).strip().replace('\n', ' '))
        sent_L.extend(sents)
        n_sent += len(sents)
    return sent_L, n_sent

file_list = list(sorted(glob(os.path.join(file_dir, '*.txt'))))

for i, file_path in enumerate(file_list):
    sents, n_sent = convert_into_sentences(open(file_path).readlines())
    print('\n'.join(sents))
    print('\n\n\n\n')
    sys.stderr.write(
        '{}/{}\t{}\t{}\n'.format(i, len(file_list), n_sent, file_path))
