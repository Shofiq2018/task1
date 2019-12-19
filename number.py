# Print 1 to 100 Number
# Create Text File
def wrile_1_100():
    f = open("shofiqul.txt", "w+")
    for i in range(1, 101):
        f.write(str(i) + "\n")
    f.close()


# console print half of the numbers
def console_half():
    filepath = 'shofiqul.txt'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while cnt <= 50:
            print("{}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1

    return cnt - 1
