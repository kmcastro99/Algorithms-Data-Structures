# run_experiments.pyt
#
# Author: Karla Castro
# Student ID: 20745522
# Email: kmcastro
# Date: 2023-11-29
# Description: This file contains the experiments that will be run for the time analysis
# input: DodgeballManager methods
# output: Plots and strings of the time analysis
#
# Use this program to run experiments and time methods that you implement
# Commenting can be light in this file
# Based on code by Oliver Schneider


import time
import random
from dodgeball_manager import DodgeballManager
from dodgeball_player import DodgeballPlayer
from list.array_list import ArrayList
import matplotlib.pyplot as plt



# Sorting experiments
def exp1_arraylist_sort():

    # make a time array
    time_array = []

    SIZE = 5000
    STEP = SIZE // 50 # 50 evenly sampled sizes

    # print header
    print(f"n|Sort Time (ms)")
    # create arrays of size n
    for n in range(0, SIZE, STEP):

        # create random array list of size n
        a = ArrayList()
        for i in range(n):
            # random integer between -1000 and 1000
            a.append(random.randint(-1000,1000))

        # setup timing
        start_time_s = time.time()
        
        # sort
        a.sort()

        # end time (should be immediately following the action)
        end_time_s = time.time()
        
        # print out recorded time in ms
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        time_array.append(d_time_ms)
        print(f"{n}|{d_time_ms}")
    return time_array, range(0,SIZE, STEP)
    

# experiment with DodgeballManager "isThrower" method
def exp2_dm_isThrower():

    # make a thrower list, and time array
    thrower_list = []
    time_array = []

    SIZE = 10000
    STEP = SIZE // 100 # 100 samples

    for i in range(0,SIZE):
        thrower_list.append(str(i))

    # create DodgeballManagers
    dm = DodgeballManager(thrower_list, ["dodger"])

    # test time for every 10 indices
    #print the header
    print("Index|isThrower Time (ms)")

    for i in range(0,SIZE, STEP):
        start_time_s = time.time()
        dm.isThrower(str(i))
        end_time_s = time.time()
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        time_array.append(d_time_ms)
        print(f"{i}|{d_time_ms}")
    return time_array, range(0,SIZE, STEP)

# experiment with DodgeballManager "nBenchedPlayers" method
def exp3_dm_nBenchedPlayers():

    # make a thrower list, and time array
    thrower_list = []
    time_array = []

    SIZE = 10000
    STEP = SIZE // 100 # 100 samples

    for i in range(0,SIZE):
        thrower_list.append(str(i))

    # create DodgeballManagers
    dm = DodgeballManager(thrower_list, ["dodger"])

    # test time for every 10 indices
    #print the header
    print("Index|nBenchedPlayers Time (ms)")

    for i in range(0,SIZE, STEP):
        start_time_s = time.time()
        dm.nBenchedPlayers()
        end_time_s = time.time()
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        time_array.append(d_time_ms)
        print(f"{i}|{d_time_ms}")
    return time_array, range(0,SIZE, STEP)

# experiment with DodgeballManager "dodge" method
def exp4_dm_dodge():

    # make a thrower list, dodger list, and time array
    thrower_list = []
    dodger_list = []
    time_array = []

    SIZE = 100000
    STEP = SIZE // 100 # 1000 samples
    # Append inputs in thrower list and dodger list
    for i in range(0,SIZE):
        thrower_list.append(str(i))
        dodger_list.append(str(i))
    
    # create DodgeballManagers
    dm = DodgeballManager(thrower_list, dodger_list)

    # test time for every 10 indices
    #print the header
    print("Index|dodge Time (ms)")
    for i in range(0,SIZE, STEP):
        start_time_s = time.time()
        dm.dodge(str(i), str(i))
        end_time_s = time.time()
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        time_array.append(d_time_ms)
        print(f"{i}|{d_time_ms}")
    return time_array, range(0,SIZE, STEP)

# experiment with DodgeballManager "hit" method
def exp5_dm_hit():

    # make a thrower list, dodger list, and time array
    thrower_list = []
    dodger_list = []
    time_array = []

    SIZE = 100000
    STEP = SIZE // 100 # 1000 samples
    # Append inputs in thrower list and dodger list
    for i in range(0,SIZE):
        thrower_list.append(str(i))
        dodger_list.append(str(i))
    
    # create DodgeballManagers
    dm = DodgeballManager(thrower_list, dodger_list)

    # test time for every 10 indices
    #print the header
    print("Index|hit Time (ms)")
    for i in range(0,SIZE, STEP):
        start_time_s = time.time()
        dm.hit(str(i), str(i))
        end_time_s = time.time()
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        time_array.append(d_time_ms)
        print(f"{i}|{d_time_ms}")
    return time_array, range(0,SIZE, STEP)

# experiment with DodgeballManager "catchBall" method
def exp6_dm_catchBall():

    # make a thrower list, dodger list, bench list, and time array
    thrower_list = []
    dodger_list = []
    bench_list = []
    time_array = []

    SIZE = 100000
    STEP = SIZE // 100 # 1000 samples

    # make a thrower list, dodger, and bench list
    for i in range(0,SIZE):
        thrower_list.append(str(i))
        dodger_list.append(str(i))
        bench_list.append(str(i))
    
    # create DodgeballManagers
    dm = DodgeballManager(thrower_list, dodger_list)

    # add bench players to the bench
    for name in bench_list:
        dm._benchList.append(DodgeballPlayer(name))

    # test time for every 10 indices
    #print the header
    print("Index|catchBall Time (ms)")
    for i in range(0,SIZE, STEP):
        start_time_s = time.time()
        dm.catchBall(str(i), str(i), str(i))
        end_time_s = time.time()
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        time_array.append(d_time_ms)
        print(f"{i}|{d_time_ms}")
    return time_array, range(0,SIZE, STEP)

# experiment with DodgeballManager "printThrower" method
def exp7_dm_printThrower():
    # make time array
    time_array = []

    SIZE = 1000
    STEP = SIZE // 100 # 100 samples

    print("Index|printThrower Time (ms)")
    for i in range(1, SIZE, STEP):
        thrower_list = []
        # append inputs in thrower list
        for j in range(i):
            thrower_list.append(str(j))
        # create DodgeballManagers
        dm = DodgeballManager(thrower_list, ['dodger'])
        # test time for every 10 indices
        #print the header
        start_time_s = time.time()
        dm.printThrowers()
        end_time_s = time.time()
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        time_array.append(d_time_ms)
        print(f"{i}|{d_time_ms}")
    return time_array, range(0,SIZE, STEP)

# experiment with DodgeballManager "printMVP" method
def exp8_dm_printMVP():
    # make a time array list
    time_array = []

    SIZE = 1000
    STEP = SIZE // 100 # 100 samples

    print("Index|printThrower Time (ms)")
    for i in range(1, SIZE, STEP):
        thrower_list = []
        dodger_list = []
        # append inputs in thrower list
        for j in range(i):
            thrower_list.append(str(j))
            dodger_list.append(str(j))
        # create DodgeballManagers
        dm = DodgeballManager(thrower_list, dodger_list)
        # test time for every 10 indices
        #print the header
        start_time_s = time.time()
        dm.printMVP()
        end_time_s = time.time()
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        time_array.append(d_time_ms)
        print(f"{i}|{d_time_ms}")
    return time_array, range(0,SIZE, STEP)

# Experiment with DodgeballManager "printSortedScores" method
def exp9_dm_printSortedScores():
    # make a time array
    time_array = []

    SIZE = 1000
    STEP = SIZE // 100 # 100 samples

    print("Index|printThrower Time (ms)")
    for i in range(1, SIZE, STEP):
        dodger_list = []
        thrower_list = []
        # append inputs in thrower list
        for j in range(i):
            thrower_list.append(str(j)) # append to thrower
            dodger_list.append(str(j)) # append to bench

        # create DodgeballManagers
        dm = DodgeballManager(thrower_list, dodger_list)
        # test time for every 10 indices
        #print the header
        start_time_s = time.time()
        dm.printSortedScores()
        end_time_s = time.time()
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        time_array.append(d_time_ms)
        print(f"{i}|{d_time_ms}")
    return time_array, range(0,SIZE, STEP)

# Experiment with DodgeballManager constructor
def exp10_dm_constructor():
    # make a thrower list, dodger list, bench list, and time array
    thrower_list = []
    dodger_list = []
    bench_list = []
    time_array = []

    SIZE = 10000
    STEP = SIZE // 100 # 1000 samples

    # make a thrower list, dodger, and bench list
    for i in range(0,SIZE):
        thrower_list.append(str(i))
        dodger_list.append(str(i))
        bench_list.append(str(i))
    
    # create DodgeballManagers
    dm = DodgeballManager(thrower_list, dodger_list)

    # add bench players to the bench
    for name in bench_list:
        dm._benchList.append(DodgeballPlayer(name))

    # test time for every 10 indices
    #print the header
    print("Index|catchBall Time (ms)")
    for i in range(0,SIZE, STEP):
        start_time_s = time.time()
        dm
        end_time_s = time.time()
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        time_array.append(d_time_ms)
        print(f"{i}|{d_time_ms}")
    return time_array, range(0,SIZE, STEP)

    print()
# Experiment 

if __name__ == "__main__":
    # call experiments here
    # Plot n vs time

    # Experiment 1
    t, x = exp1_arraylist_sort()
    plt.plot(x,t)
    plt.title("ArrayList Sort Time")
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.show()

    # Experiment 2
    t, x = exp2_dm_isThrower()
    plt.plot(x,t)
    plt.title("DodgeballManager isThrower Time")
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.show()

    # Experiment 3
    t, x = exp3_dm_nBenchedPlayers()
    plt.plot(x,t)
    plt.title("DodgeballManager nBenchedPlayers Time")
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.show()

    # Experiment 4
    t, x = exp4_dm_dodge()
    plt.plot(x,t)
    plt.title("DodgeballManager dodge Time")
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.show()

    # Experiment 5
    t, x = exp5_dm_hit()
    plt.plot(x,t)
    plt.title("DodgeballManager hit Time")
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.show()

    # Experiment 6
    t, x = exp6_dm_catchBall()
    plt.plot(x,t)
    plt.title("DodgeballManager catchBall Time")
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.show()

    # Experiment 7
    t, x = exp7_dm_printThrower()
    plt.plot(x,t)
    plt.title("DodgeballManager printThrower Time")
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.show()

    # Experiment 8
    t, x = exp8_dm_printMVP()
    plt.plot(x,t)
    plt.title("DodgeballManager printMVP Time")
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.show()

    # Experiment 9
    t, x = exp9_dm_printSortedScores()
    plt.plot(x,t)
    plt.title("DodgeballManager printSortedScores Time")
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.show()

    # Experiment 10
    t, x = exp10_dm_constructor()
    plt.plot(x,t)
    plt.title("DodgeballManager Constructor Time")
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.show()