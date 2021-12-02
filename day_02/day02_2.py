#/usr/bin/python3

horizontal = 0
depth = 0
aim = 0
puzzlelist = []
commands = ("forward","down","up")
command =[]

def process(inputfile):
    """
    blub blub
    """
    global puzzlelist,command
    global horizontal
    global depth, aim

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
            # forward command
            if action[0] == commands[0]:
                horizontal += int(action[-1])
                depth += (aim * int(action[-1]))   
                print("H: %3i A: %3i" % (horizontal,aim))
            #down command    
            if action[0] == commands[1]:
                aim += int(action[-1])
                print("depth: %3i aim: %3i" % (depth,aim))
            #up command    
            if action[0] == commands[2]:
                aim -= int(action[-1])
                print("depth: %3i aim: %3i" % (depth,aim))
                            
        
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
    
    
