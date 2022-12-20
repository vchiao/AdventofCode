from string import ascii_letters as let

def get_input():
    with open('input.txt','r') as inp: #_test
        lines = inp.read().splitlines()
        return lines

def t1(inp):
    p = get_prior()
    sum = 0
    for line in inp:
        ruck1, ruck2 = splitter(line)
        common = list(set(ruck1)&set(ruck2))
        for a in common:
            sum += p[a]
    return sum

def t2(inp):
    p = get_prior()
    sum = 0
    group=[]
    badge = []
    for line in inp:
        group.append(line)
        if len(group)==3:
            badge += list(set(group[0])&set(group[1])&set(group[2]))
            # print(group, badge)
            group=[]

    for i in badge:
        sum += p[i]

    return sum

def splitter(line):
    halfway = len(line)//2
    ruck1 = line[:halfway]
    ruck2 = line[halfway:]
    return ruck1, ruck2

def get_prior():
    count = 1
    prior={}
    for i in let:
        prior[i] = count
        count+=1
    return prior

inp = get_input()
print(t2(inp))