import sys
try:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        n_tower = lines[0]
        n_op = lines[1]
        
        print int(lines[0]) + int(lines[1])
except:
    pass