import argparse
import sys
import math


def read_fasta(filename: str) -> dict:
    id_dna_map = {}

    with open(filename, 'r') as f:
        lines = f.readlines()

    if not lines[0].startswith('>'):
        sys.exit('Not a fasta file!')

    curr_id = -1
    for l in lines:
        if l.startswith('>'):
            curr_id += 1
            id_dna_map[curr_id] = ''
        else:
            id_dna_map[curr_id] += l.rstrip()
    return id_dna_map

def concat_str(s1: str, s2: str) -> str:
    m = min(len(s1), len(s2))
    for i in range(m, 0, -1):
        if s1[-i:] == s2[:i]:
            return s1 + s2[i:]

parser = argparse.ArgumentParser(description='Construct genome assembly of the reads input')
parser.add_argument('input', type=str, help='Input fasta file')
parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout, help='Output file')

args = parser.parse_args()

id_dna_map = read_fasta(args.input)

n = len(id_dna_map)

G = [[0 for _ in range(n)] for _ in range(n)]
str_len = len(id_dna_map[0])
threshold = math.ceil(str_len / 2) # half the read length

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        is_overlap = False
        cut = 0
        for k in range(threshold, str_len):
            if id_dna_map[i][-k:] == id_dna_map[j][:k]:
                is_overlap = True
                cut = k
                break
        if is_overlap:
            G[i][j] = cut

# find start and end
rowsum = [0]*n
colsum = [0]*n
for i in range(n):
    for j in range(n):
        rowsum[i] += G[i][j]
        colsum[j] += G[i][j]

start = -1
end = -1
for i in range(n):
    if colsum[i] == 0:
        start = i
    if rowsum[i] == 0:
        end = i

contig = id_dna_map[start]
i = start
while i != end:
    for j in range(n):
        if G[i][j] > 0:
            s1 = id_dna_map[i]
            s2 = id_dna_map[j]
            contig += s2[G[i][j]:]
            i = j

out = args.output
out.write(contig + '\n')
