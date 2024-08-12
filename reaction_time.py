import time
import random


def start():
    enter=input("Press enter to start")
    get_queue()

def get_queue():
    random_num = random.randint(1,10)
    time.sleep(random_num)
    count_start_time=time.time()
    click(count_start_time)

def click(count_start_time):
    enter_again=input("click")
    end_time(count_start_time)

def end_time(count_start_time):
    count_end_time=time.time()
    calculation(count_end_time,count_start_time)

def calculation(count_start_time,count_end_time):
    reaction_time=count_start_time-count_end_time
    formatted_time = "{:.3f}".format(reaction_time)
    print("Your Reaction Time Is: ", formatted_time, "ms")
    write(formatted_time)

def write(formatted_time):
    datetime=time.ctime(time.time())
    with open("reaction time report.txt", "a") as f:
        f.write(formatted_time + "ms on " + datetime + "\n")

start()
