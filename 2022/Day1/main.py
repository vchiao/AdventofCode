import itertools as it

def get_input():
    with open('input1.txt','r') as inp:
        lines = inp.readlines()
        print(lines)
        return lines

def get_reindeers():
    reindeers = []
    with open('input1.txt','r') as inp:
        for key, group in it.groupby(inp, lambda line: line.startswith('\n')):
            if not key:
                group = list(group)
                group = [int(i) for i in group]
                reindeers.append(group)
    return reindeers

def get_most_calories(reindeers):
    max_cal=0
    max_reindeer=0
    for reindeer in reindeers:
        cal = sum(reindeer)
        if cal > max_cal:
            max_cal = cal
            max_reindeer=reindeer

    return (max_reindeer, max_cal)

def get_top3(elves):
    top3 = []
    copy_elves = elves[:]

    while len(top3)<3:
        max1 = get_most_calories(copy_elves)
        top3.append(max1[1])
        copy_elves.remove(max1[0])

    return top3



# def count_reindeers(my_input):
#     reindeer_count = 0
#     line_idx = 0
#
#     if len(my_input)>0:
#         reindeer_count+=1
#
#     while line_idx < len(my_input)-1:
#         if my_input[line_idx]!="\n" and my_input[line_idx+1]=="\n":
#             reindeer_count += 1
#         line_idx += 1
#     print(reindeer_count)


reindeers = get_reindeers()
print(get_most_calories(reindeers))
print(sum(get_top3(reindeers)))

# count_reindeers(get_input())
