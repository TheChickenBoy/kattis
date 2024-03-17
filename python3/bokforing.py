from sys import stdin, stdout

n,q = map(int,stdin.readline().split())
people = [[0,0]]*n
reset = [-1,0]
i=0
line = stdin.readline()
while line:
    information = line.split()
    if information[0] == "SET":
        people[int(information[1])-1] = [i,int(information[2])]
    elif information[0] == "PRINT":
        tmp_idx = int(information[1])-1
        if people[tmp_idx][0] > reset[0]:
            stdout.write(str(people[tmp_idx][1]))
        else:
            stdout.write(str(reset[1]))
        stdout.write("\n")
    elif information[0] == "RESTART":
        reset = [i, int(information[1])]
    line = stdin.readline()
    i+=1