def read_file(name):
    with open(name, encoding='utf-8') as f:
        lines = (f.readlines())
        lines.insert(0, str(len(lines)) + '\n')
        lines.insert(0, name + '\n')
    return lines


def general_file(name1, name2, name3):
    f1 = read_file(name1)
    f2 = read_file(name2)
    f3 = read_file(name3)
    list_f = [f1, f2, f3]
    sorted_list = sorted(list_f, key=lambda l: (len(l), l))
    with open('general.txt', 'w', encoding='utf-8') as f:
        for file in sorted_list:
            for line in file:
                f.write(line)


general_file('1.txt', '2.txt', '3.txt')