def get_input():
    with open('input.txt','r') as inp: #_test
        lines = inp.read().splitlines()
        return lines

def visible(inp):
    """
    inp[i] == column
    inp[i][j] where j is row
    :param inp:
    :return:
    """
    rows = len(inp)
    cols = len(inp[0])

    vis = 0
    score=[]


    for i in range(rows):
        for j in range(cols):
            try:
                tree = inp[i][j] #inp[1][2]
                u = [inp[up][j] for up in range(i)]
                d = [inp[down+i+1][j] for down in range(rows-i-1)]
                l = [inp[i][left] for left in range(j)]
                r = [inp[i][right + j+1] for right in range(cols-j-1)]


                if tree > max(l) or tree > max(r) or tree > max(u) or tree > max(d):
                    vis+=1

                up_view = view(tree, reversed(u))
                d_view = view(tree, d)
                l_view = view(tree, reversed(l))
                r_view = view(tree, r)

                score.append(up_view*d_view*l_view*r_view)

            except ValueError or IndexError:
                vis += 1
                # pass
            # print(tree, u, d, l, r)
    return vis, max(score)

def view(tree,list):
    v=0
    # print("tree is " + str(tree))
    for x in list:
        # print("x is " + x)
        v += 1
        if x >= tree:
            # print("v is " + str(v))
            return v

    # print("v is "+ str(v))
    return v

input = get_input()
print(visible(input))
