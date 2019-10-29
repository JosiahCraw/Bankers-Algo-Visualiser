import os
def printAll(banner, avail, processes, curr_pro):
    print(banner)
    print(" ")
    print("Available")
    out_str = '[ '
    for number in avail:
        out_str = out_str + str(number) + " "
    out_str = out_str + ']'
    print(out_str)
    print(" ")
    print(banner)
    print(" ")
    print("Required to Complete: ")
    print(" ")
    i = 0
    for process in processes:
        string_out = 'P' + str(i) + ' [ '
        i = i + 1
        for num in process:
            string_out = string_out + str(num) + " "
        string_out = string_out + ']'
        print(string_out)
    print(" ")
    print(banner)
    print(" ")
    print("Currently Used")
    i = 0
    for curr in curr_pro:
        string = 'P' + str(i) + ' [ '
        i = i + 1
        for num in curr:
            string = string + str(num) + " "
        string = string + ']'
        print(string)
    print(" ")
    print(banner)
    print(" ")

if __name__ == "__main__":
    banner = "+-----------------------------+"
    print(banner)
    avail = input("Enter avalible resources: ")
    print(banner)
    avail = avail.split()
    for i in range(0, len(avail)):
        avail[i] = int(avail[i])
    processes = list()
    curr_pro = list()
    more = True
    while more:
        print(banner)
        print(" ")
        temp = input("Enter Process Requirements: ")
        print(" ")
        if temp == "":
            more = False
            continue
        temp2 = input("Enter Current Allocations: ")
        print(" ")
        print(banner)
        temp = temp.split()
        temp2 = temp2.split()
        for i in range(0, len(temp)):
            temp[i] = int(temp[i])
            temp2[i] = int(temp2[i])
        curr_pro.append(temp2)
        processes.append(temp)
    
    exit = False
    while not exit:
        printAll(banner, avail, processes, curr_pro)
        got_char = input("What Process to complete? ")
        print(" ")
        if got_char == 'q':
            exit = True
            continue
        try:
            number = int(got_char)
        except ValueError:
            continue
        try:
            current_process = processes[number]
            curr_pro_current = curr_pro[number]
        except IndexError:
            print("Try Again no process of that number")
            continue
        
        for i in range(0, len(current_process)):
            avail[i] = avail[i] - current_process[i]
        if min(avail) < 0:
            print(banner)
            _ = os.system("clear")
            print(" ")
            print("Not enough resourses")
            for i in range(0, len(current_process)):
                avail[i] = avail[i] + current_process[i]
            continue
        for i in range(0, len(avail)):
            avail[i] = avail[i] + current_process[i] + curr_pro_current[i]
            current_process[i] = 0
            curr_pro_current[i] = 0
        _ = os.system("clear")
            

 
