import argparse
import sys

parser = argparse.ArgumentParser(description='Count symbols A, C, G, T occurint in the input string')
parser.add_argument('input', type=str, help='Input fasta file')
parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout, help='Output file')

args = parser.parse_args()

with open(args.input, 'r') as f:
    dna = f.read().rstrip()

f = args.output
f.write(dna.replace('T', 'U'))
