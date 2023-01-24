import os
import time
import pyautogui

def check_schedule():
    """
    Check if schedule.csv file exists. If not, exit the program.
    """
    if os.path.isfile('schedule.csv'):
        print("schedule.csv file found. Continuing...")
        time.sleep(2)
    else:
        print("No schedule.csv file found. Please create one and try again.")
        exit()

def check_schedule_format():
    """
    Check if schedule.csv file has the correct format. If not, exit the program.
    """
    f = open('schedule.csv', 'r')
    for line in f:
        if line.count(',') != 2:
            print("Invalid schedule.csv format. Please check the file and try again.")
            f.close()
            exit()

def read_schedule():
    """
    Read schedule.csv file and return a list of tasks.
    """
    f = open('schedule.csv', 'r')
    fields = f.readline()
    lines = f.readlines()
    tasks = []
    for line in lines:
        tasks.append(line.split(','))
    f.close()
    return tasks

def type_tasks(tasks):
    """
    Type tasks in the Telegram bot
    """
    print("Starting to type tasks...")
    print("Bring Cursor to the Telegram bot in 10 seconds...")
    time.sleep(10)
    for task in tasks:
        print("Typing task: " + task[0])
        pyautogui.typewrite("/add", interval=0.1)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.typewrite(task[0], interval=0.1)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.typewrite(task[1], interval=0.1)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.typewrite(task[2].rstrip('\n'), interval=0.1)
        pyautogui.press('enter')
        time.sleep(3)

def main():
    check_schedule()
    check_schedule_format()
    tasks = read_schedule()
    type_tasks(tasks)
    print("Program finished.")

main()