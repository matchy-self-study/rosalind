# Overlap Graphs

<details><summary><b>A Brief Introduction to Graph Theory</b></summary>

Networks arise everywhere in the practical world, especially in biology. Networks are prevalent in popular applications such as modeling the spread of disease, but the extent of network applications spreads far beyond popular science. Our first question asks how to computationally model a network without actually needing to render a picture of the network.

First, some terminology: <b>graph</b> is the technical term for a network; a graph is made up of hubs called <b>nodes</b> (or <b>vertices</b>), pairs of which are connected via segments/curves called <b>edges</b>. If an edge connects nodes `v` and `w`, then it is denoted by `{v,w}` (or equivalently `{w,v}`).

An edge `{v,w}` is <b>incident</b> to nodes v and w; we say that v and w are adjacent to each other;

The <b>degree</b> of `v` is the number of edges incident to it;

A <b>walk</b> is an ordered collection of edges for which the ending node of one edge is the starting node of the next (e.g., `{v1,v2}, {v2,v3}, {v3,v4}`, etc.);

A <b>path</b> is a walk in which every node appears in at most two edges;

<b>Path length</b> is the number of edges in the path;

A <b>cycle</b> is a path whose final node is equal to its first node (so that every node is incident to exactly two edges in the cycle); and

the <b>distance</b> between two vertices is the length of the shortest path connecting them.

<b>Graph theory</b> is the abstract mathematical study of graphs and their properties.
</details>

## Problem

A graph whose nodes have all been labeled can be represented by an **adjacency list**, in which each row of the list contains the two node labels corresponding to a unique edge.

A **directed graph** (or digraph) is a graph containing **directed edges**, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by `(v,w)` (but not by `(w,v)`). A **directed loop** is a directed edge of the form `(v,v)`.

For a collection of strings and a positive integer `k`, the **overlap graph** for the strings is a directed graph `Ok` in which each string is represented by a node, and string `s` is connected to string `t` with a directed edge when there is a length `k` suffix of `s` that matches a length `k` prefix of `t`, as long as `s≠t`; we demand `s≠t` to prevent directed loops in the overlap graph (although directed cycles may be present).

- **Given**: A collection of DNA strings in FASTA format having total length at most 10 kbp.
- **Return**: The adjacency list corresponding to `O3`. You may return edges in any order.

## Sample Dataset

```fasta
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
```

## Sample Output

```text
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
```

<details>
<summary>
<b>Note on Visualizing Graphs</b>
</summary>
If you are looking for a way to actually visualize graphs as you are working through the Rosalind site, then you may like to consider Graphviz, a cross-platform application for rendering graphs.
</details>
