presents = []

with open('./input', 'r') as f:
    for line in f:
        l,w,h = map(int, line.strip().split('x'))
        presents.append((l,w,h))

packing_paper_area = sum([2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l) for l,w,h in presents])
print(packing_paper_area)

ribbon_length = sum([2*sorted([l, w, h])[0] + 2*sorted([l, w, h])[1] + l*w*h for l, w, h in presents])
print(ribbon_length)