#!/bin/bash

echo "Provide problem category."
echo "Available: AH (AlgorithmicHeights), BA (BioinformaticsArmory), BS(BioinformaticsStronghold)"

read -p "Enter problem category (AH/BA/BS): " d

read -p "Enter rosalind problem name (e.g. RSTR): " prob

dir=$(case "${d}" in
    (AH) echo "AlgorithmicHeights";;
    (BA) echo "BioinformaticsArmory";;
    (BS) echo "BioinformaticsStronghold";;
esac)

parent="${dir}/${prob}"

mkdir -p "${parent}" && touch "${parent}/README.md" && touch "${parent}/solution.py"
mkdir -p "${parent}/inputs"
mkdir -p "${parent}/outputs"
