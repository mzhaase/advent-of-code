First implementation was like this:
- for line in file, for char in line, create a dictionary where the key is the coord and the value is the number 0-9. runtime: 1 ms
- from that, create a graph from every node to all four neighboring nodes, where the node number (0-9) is exactly 1 bigger. runtime: 5 ms
- for all combinations of zeroes and nines, calculate all simple paths, if the path if of length 10, it is a viable answer. runtime: 4.4 s.

- changing from
```
for nine in nines:
        paths = nx.all_simple_paths(G, source=zero, target=nine, cutoff=10)
```

to
```
paths = nx.all_simple_paths(G, source=zero, target=nines, cutoff=10)
```

and letting the path algorithm handle all nines, decreases this runtime to 71 ms.

Doing this part with multiprocessing, one process per zero in zeroes, reduces total time to 46 ms.
