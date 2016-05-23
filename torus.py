words = {}
for i in file('words.txt').readlines():
    words[i[:-1]] = 1

slots = [{}, {}, {}, {}, {}, {}]
for i in words.keys():
    for j in range(5):
        if not slots[j].has_key(i[j]):
            slots[j][i[j]] = {}
        slots[j][i[j]][i] = 1

h = {}
for i in words.keys():
    if i.endswith('h'):
        h[i] = 1

od = {}
for i in words.keys():
    if i.endswith('od'):
        od[i] = 1

def matches(a, b):
    x = True
    for i in range(len(a)):
        if b[i] != '.' and a[i] != b[i]:
            x = False
            break
    return x

def any_matches(pattern):
    for i in words.keys():
        if matches(i, pattern):
            return True
    return False

def count_matches(w, pattern):
    n = 0
    for i in w.keys():
        if matches(i, pattern):
            n += 1
    return n

h_poss = {}

for i in h:
    if any_matches('...o%s' % i[0]) and any_matches('..r%s.' % i[1]) and any_matches('.u%s..' % i[2]) and any_matches('s%s...' % i[3]):
        h_poss[i] = 1
        print 'H_POSS\t%s' % i

od_poss = {}
for i in od:
    if any_matches('..r%s.' % i[0]) and any_matches('.u%s..' % i[1]) and any_matches('s.%s..' % i[2]):
        h_poss[i] = 1
        print 'OD_POSS\t%s' % i

if 0 :
    odh_poss = {}
    h = h.keys()
    h.sort()
    od = od.keys()
    od.sort()
    f = file('odh.txt','w')
    for i in h:
        for j in od:
            if any_matches('...o%s' % i[0]) and any_matches('..r%s%s' % (i[1], j[0])) and any_matches('.u%s%s.' % (i[2], j[1])) and any_matches('s%s%s..' % (i[3], j[2])):
                odh_poss[(i, j)] = 1
                print 'ODH_POSS\t%s\t%s\t' % (i, j)
                f.write('%s\t%s\n' % (i, j))
    f.close()
if 0 :
    odh = odh_poss.keys()
    odh.sort()
    for ij in odh:
        i, j = ij
        for k in slots[3]['o'].keys():
            if any_matches('%s..o%s' % (k[4], i[0])) and any_matches('..r%s%s' % (i[1], j[0])) and any_matches('.u%s%s%s' % (i[2], j[1], k[0])) and any_matches('s%s%s%s.' % (i[3], j[2], k[1])):
                print 'ROW4_POSS\t%s\t%s\t%s' % (i, j, k)


if 0 :
    row5 = []
    for i in words.keys():
        if matches(i, '.en..'):
            row5.append(i)


    for l in file('odh.txt').readlines():
        i, j = l[:-1].split()
        for k in row5:
            if any_matches('.%s.o%s' % (k[3], i[0])) and any_matches('%s.r%s%s' % (k[4], i[1], j[0])) and any_matches('.u%s%s.' % (i[2], j[1])) and any_matches('s%s%s.%s' % (i[3], j[2], k[0])):
                    print 'ROW5_POSS\t%s\t%s\t%s' % (i, j, k)

if 0 :
    for down in ('homer', 'holes'):
        row4p = []
        for i in words.keys():
            if matches(i, '..%so.' % down[2]):
                row4p.append(i)
        for i in file('row5.txt').readlines():
            row2, row3, row5 = i[:-1].split()
            for row4 in row4p:
                print 'ROW6_COUNT\t%s\t%s\t%s\t%s\t%s\t%d\t%d\t%d\t%d' % (down, row2, row3, row4, row5, count_matches(slots[3]['o'], '%s%s.o%s' % (row4[4], row5[3], row2[0])), count_matches(slots[2]['r'], '%s.r%s%s' % (row5[4], row2[1], row3[0])), count_matches(slots[1]['u'], '.u%s%s%s' % (row2[2], row3[1], row4[0])), count_matches(slots[0]['s'], 's%s%s%s%s' % (row2[3], row3[2], row4[1], row5[0])))

row6homer = []
row6holes = []
for i in words.keys():
    if matches(i, 'ru...'):
        row6homer.append(i)
    if matches(i, 'su....'):
        row6holes.append(i)

for i in file('row2345.txt').readlines():
    down, row2, row3, row4, row5 = i[:-1].split()
    if 'homer' == down:
        row6p = row6homer
    else:
        row6p = row6holes
    for row6 in row6p:
        x = count_matches(slots[3]['o'], '%s%s%so%s' % (row4[4], row5[3], row6[2], row2[0])) + count_matches(slots[2]['r'], '%s%sr%s%s' % (row5[4], row6[3], row2[1], row3[0])) + count_matches(slots[1]['u'], '%su%s%s%s' % (row6[4], row2[2], row3[1], row4[0])) + count_matches(slots[0]['s'], 's%s%s%s%s' % (row2[3], row3[2], row4[1], row5[0]))
        if 3 != x:
            continue
        row1 = 'torus'
        d1 = down
        d2 = 'donut'
        d3 = '%s%s%so%s' % (row4[4], row5[3], row6[2], row2[0])
        d4 = '%s%sr%s%s' % (row5[4], row6[3], row2[1], row3[0])
        d5 = '%su%s%s%s' % (row6[4], row2[2], row3[1], row4[0])
        d6 = 's%s%s%s%s' % (row2[3], row3[2], row4[1], row5[0])
        bad = None
        if not d3 in words:
            bad = d3
        if not d4 in words:
            bad = d4
        if not d5 in words:
            bad = d5
        if not d6 in words:
            bad = d6
        print 'SOL3\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (bad, row1, row2, row3, row4, row5, row6, d1, d2, d3, d4, d5, d6)
