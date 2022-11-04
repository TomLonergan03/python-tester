from sys import argv
from time import time


class colours:
    HEADER = '\033[95m'
    PASS = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


total = 0
passed = 0
start_time = 0


def runTests(*tests):
    global total, passed, start_time
    total = 0
    passed = 0
    start_time = time()
    for test in tests:
        print(colours.HEADER + test.__name__ + colours.ENDC)
        test()
    printResult()


def assertEqual(name, correct_result, function=lambda x: x, *args, **kwargs):
    global total, passed
    total = total + 1
    testname = "Test " + str(total) + ": " + str(name)
    print(f"{testname:<50}", sep="", end=" ")
    actual_result = function(*args, **kwargs)
    if (correct_result == actual_result):
        print(f'{(colours.PASS + "Passed" + colours.ENDC):>10}')
        passed = passed + 1
    else:
        print(f'{(colours.FAIL + "Failed" + colours.ENDC):>10}')
        print("Expected\n", correct_result, "\ngot\n", actual_result)


def printResult():
    global total, passed
    result = round(passed/total*100)

    if result == 100:
        status = colours.PASS
    else:
        status = colours.FAIL

    print(f'{(status + str(passed) + " out of " + str(total) + " tests passed in " + str(round((time()-start_time), 4)) + " seconds"):<50}' +
          f'{(str(result) + "%" + colours.ENDC):>14}')
