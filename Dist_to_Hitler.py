import typing as T
from collections import deque 

Hitler_id = 6611
Adjencency_dict = {}
Pages = {}

Too_far = []

with open("cswiki-links-small.csv", 'rt') as f:
    f.readline() # skip header

    for line in f:
        fr, to = line.strip().split(',')
        fr = int(fr)
        to = int(to)

        if not to in Adjencency_dict:
            Adjencency_dict[to] = [fr]
        else:    
            Adjencency_dict[to].append(fr)
        
        Pages[to] = float('inf')
        Pages[fr] = float('inf')

print('read all of input')


# Wide search
Pages[Hitler_id] = 0
Visited = set([Hitler_id])

Qeue = deque([6611])

index = 1
while len(Qeue) > 0:
    index += 1
    if index % 50 == 0:
        print(index)
        print('l:',len(Qeue))
        print('visited:',len(Visited))

    page = Qeue.popleft()
    Visited.add(page)
    distance = Pages[page] + 1

    if page in Adjencency_dict:
        for conex in Adjencency_dict[page]:
            if not conex in Visited:
                Qeue.append(conex)
                Pages[conex] = distance 

                if distance > 6:
                    Too_far.append({
                        'page_id' : conex,
                        'distance': distance 
                    }) 
print('pocet moc vzdalenych:',len(Too_far))
print(Visited)