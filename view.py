def show_all(all):
    lst=[]
    for i, p in enumerate(all):
        smt = str(i+1)+') '+' '.join(p)
        lst.append(smt)

    return '\n'.join(lst)


def searching(all, message):
    for p in all:
        if p[0].lower() == message:
            return ' '.join(p)