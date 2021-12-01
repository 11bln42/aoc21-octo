#/usr/bin/python3

result = 0
puzzlelist = []

def process(inputfile):
    """
    blub blub
    """
    global puzzlelist
    global result

    with open(inputfile) as file:
        #convert file input as list
        for line in file:
            puzzlelist.append(line.strip())

    items = len(puzzlelist)
    puzzlelist
    
    print("puzzle contain today: %3i items" % items)

    for i in range(1,items):
        if puzzlelist[i-1] < puzzlelist[i]:
            result +=1
            
    print("result for puzzle 1: %3i"% result) 


#
#
if __name__ == "__main__":
    # execute only if run as a script
    #main()
    infile ="input-example.txt"
    process(infile)
    
