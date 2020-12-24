import argparse
import sys

parser = argparse.ArgumentParser(description='Count symbols A, C, G, T occurint in the input string')
parser.add_argument('input', type=str, help='Input fasta file')
parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout, help='Output file')

args = parser.parse_args()

with open(args.input, 'r') as f:
    dna = f.read().rstrip()

nt_count = {}

for c in dna:
    try:
        nt_count[c] += 1
    except:
        nt_count[c] = 1

f = args.output
f.write(f"{nt_count['A']} {nt_count['C']} {nt_count['G']} {nt_count['T']}\n")
