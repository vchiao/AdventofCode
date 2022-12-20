
def get_input():
    with open('input.txt','r') as inp:
        lines = inp.read().splitlines()
        return lines

def main(inp):
    directories = []
    for line in inp:
        if line.startswith()