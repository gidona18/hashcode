from collections import namedtuple

Pic = namedtuple('Pic', ['idx','type','tags'])

def read_file(path):
    lines = []
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    lines = [line.split() for line in lines[1:]]
    pics = [Pic(idx, pic[0], pic[2:]) for idx, pic in enumerate(lines)]
    return (pics)

def main(ipath, opath):
    # Read picture tags from file.
    pics = read_file(ipath)

    # Sort tags.
    idx = 0;
    while idx < len(pics):
        pics[idx] = Pic(
            pics[idx].idx,
            pics[idx].type,
            sorted(pics[idx].tags))
        idx += 1

    # Sort pics by tags.
    pics.sort(key=lambda p: p.tags)

    lst = []
    idx = 0;
    while idx < len(pics):
        try:
            if pics[idx].type == 'H':
                lst.append([pics[idx]])
            elif pics[idx].type == 'V' and pics[idx+1].type == 'H':
                pics[idx], pics[idx+1] = pics[idx+1], pics[idx]
                lst.append([pics[idx]])
            elif pics[idx].type == 'V' and pics[idx+1].type == 'V':
                lst.append([pics[idx], pics[idx+1]])
                idx += 1
        except IndexError:
                pass
        idx += 1
    
    # Write
    with open(opath, 'w') as f:
        f.write(str(len(lst)) + '\n')
        idx = 0;
        while idx < len(lst):
            if lst[idx][0].type == 'H':
                f.write(str(lst[idx][0].idx) + '\n')
            if lst[idx][0].type == 'V':
                f.write(
                    str(lst[idx][0].idx) + ' ' +
                    str(lst[idx][1].idx) + '\n')
            idx += 1

main('a_example.txt', 'a_out.txt')
main('b_lovely_landscapes.txt', 'b_out.txt')
main('c_memorable_moments.txt', 'c_out.txt')
main('d_pet_pictures.txt', 'd_out.txt')
main('e_shiny_selfies.txt', 'e_out.txt')
