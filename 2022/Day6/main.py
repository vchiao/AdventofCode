
def get_input():
    with open('input.txt','r') as inp:
        lines = inp.readline()
        print(lines)
        return lines

def subroutine(inp):
    char_count = 0
    length = len(inp)

    while char_count < (length -14):
        segm = inp[char_count:char_count+14]
        print(segm)
        sub_seg = []
        for i in range(14):
            print(segm[i])
            if not segm[i] in sub_seg:
                sub_seg.append(segm[i])
                if len(sub_seg) == 14:
                    return char_count+14
            else:
                char_count+=1


input = get_input()
print(subroutine(input))
