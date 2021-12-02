#/usr/bin/python3

horizontal = 0
depth = 0
puzzlelist = []
commands = ("forward","down","up")
command =[]

def process(inputfile):
    """
    blub blub
    """
    global puzzlelist,command
    global horizontal
    global depth

    with open(inputfile) as file:
        #convert file input as list
        for line in file:
            line.split("\n")
            print(line)
            command = line.split(" ")
            print(command)
            puzzlelist.append(command)
            puzzlelist
    items = len(puzzlelist)
    print(puzzlelist)
    
    print("puzzle contain today: %3i items" % items)

    for i in range(0,items):
        action = puzzlelist[i]
        print( action)
        if action[0] in commands:
            if action[0] == commands[0]:
                #print("a: % h: %3i" % action[0],horizontal)
                horizontal += int(action[-1])
                print(horizontal)
            if action[0] == commands[1]:
                depth += int(action[-1])
                print(depth)
            if action[0] == commands[2]:
                depth -= int(action[-1])
                print(depth)
            
        
    result = horizontal * depth
    type(result)
            
    print("result for puzzle 1 of day2: %3i"% result) 


#
#
if __name__ == "__main__":
    # execute only if run as a script
    #main()
    infile ="input.txt"
    process(infile)
    
    
