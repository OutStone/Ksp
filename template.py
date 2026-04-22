import typing as T

def read_links(file_name = "cswiki-links.csv") -> T.Generator[tuple[int, int]]:
    with open(file_name, 'rt') as f:
        f.readline() # skip header
        for line in f:
            fr, to = line.strip().split(',')
            yield int(fr), int(to)


def read_titles(file_name = "cswiki-titles.csv") -> dict[int, str]:
    result = {}
    with open(file_name, 'rt') as f:
        f.readline() # skip header
        for line in f:
            id, to = line.strip().split(',', maxsplit=1)
            result[int(id)] = to
    return result

titles = read_titles()

for fr, to in read_links():
    if to == 6611:
        print(f"Hitler linkován z: {fr} {titles[fr]}")

