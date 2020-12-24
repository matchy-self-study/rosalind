import argparse
import sys

def read_fasta(filename: str) -> dict:
    id_dna_map = {}

    with open(filename, 'r') as f:
        lines = f.readlines()

    if not lines[0].startswith('>'):
        sys.exit('Not a fasta file!')

    curr_id = ''
    for l in lines:
        if l.startswith('>'):
            curr_id = l[1:].rstrip()
            id_dna_map[curr_id] = ''
        else:
            id_dna_map[curr_id] += l.rstrip()

    return id_dna_map

parser = argparse.ArgumentParser(description='Construct level 3 overlap graph for the given input fastafile and print all edges to file')
parser.add_argument('input', type=str, help='Input fasta file')
parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout, help='Output file')

args = parser.parse_args()

id_dna_map = read_fasta(args.input)

ids = list(id_dna_map.keys())
n = len(id_dna_map)

G = [[0 for _ in range(n)] for _ in range(n)]
k = 3

for i in range(n):
    id1 = ids[i]
    for j in range(n):
        if i == j:
            continue
        id2 = ids[j]
        is_overlap : bool = id_dna_map[id1][-k:] == id_dna_map[id2][:k]
        if is_overlap:
            G[i][j] = 1

out = args.output
for i in range(n):
    for j in range(n):
        if G[i][j] > 0:
            out.write(f'{ids[i]} {ids[j]}\n')
