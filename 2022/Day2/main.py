import itertools as it

"""
a = rock
b = paper
c = scissors

x = rock
y = paper
z = scissors
"""

def get_input():
    with open('input1.txt','r') as inp:
        lines = inp.readlines()
        print(lines)
        return lines

# def get_total(game):
#     score = 0
#     for round in game:
#         score += get_score(round)
#         print(score)
#     return score
#
# def get_score(round):
#     my_play = round[2]
#     my_pts = {'X': 1, 'Y': 2, 'Z': 3}
#     return my_pts[my_play] + round_points(round)
#
#
# def round_points(round):
#     pl1 = round[0]
#     pl2 = round[2]
#     draw_dict = {'A':'X','B':'Y','C':'Z'}
#
#     if draw_dict[pl1] == pl2:
#         return 3
#     elif won_result(pl1, pl2):
#         return 6
#     else:
#         return 0
#
# def won_result(pl1, pl2):
#     # rock
#     if pl1 == 'A':
#         if pl2 == 'Y':
#             return True
#         elif pl2 == 'Z':
#             return False
#     # paper
#     elif pl1 == 'B':
#         if pl2 == 'Z':
#             return True
#         elif pl2 == 'X':
#             return False
#     # scissors
#     elif pl1 == 'C':
#         if pl2 == 'X':
#             return True
#         elif pl2 == 'Y':
#             return False

"""
a = rock
b = paper
c = scissors

x = lose
y = draw
z = win
"""

def get_total(game):
    score = 0
    for round in game:
        score += get_score(round)
        print(score)
    return score

def get_score(round):
    result = round[2]
    round_pts = {'X': 0, 'Y': 3, 'Z': 6}
    return (round_pts[result] + my_play(round))

def my_play(round):
    ply1 = round[0]
    result = round[2]
    my_pts = {'A':1, 'B':2, 'C':3}

    #draw
    if result == 'Y':
        return my_pts[ply1]
    #lose
    elif result =='X':
        if ply1 == 'A':
            return my_pts['C']
        elif ply1 == 'B':
            return my_pts['A']
        elif ply1 == 'C':
            return my_pts['B']
    #Win
    elif result =='Z':
        if ply1 == 'A':
            return my_pts['B']
        elif ply1 == 'B':
            return my_pts['C']
        elif ply1 == 'C':
            return my_pts['A']



input = get_input()
print(get_total(input))
