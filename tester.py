from sys import argv
from time import time


class colours:
    HEADER = '\033[95m'
    PASS = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    WARNING = '\033[93m'


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


def test(name, correct_result="NOT IMPLEMENTED", function=lambda x: x, *args, **kwargs):
    global total, passed
    total = total + 1

    if (correct_result == "NOT IMPLEMENTED"):
        testname = "Test " + str(total) + ": " + name
        print(f"{testname:<50}", sep="", end=" ")
        print(f'{(colours.WARNING + "NOT IMPLEMENTED" + colours.ENDC):>10}')
        return

    testname = "Test " + str(total) + ": " + name
    print(f"{testname:<50}", sep="", end=" ")
    test_start_time = time()
    try:
        actual_result = function(*args, **kwargs)
    except Exception as e:
        actual_result = e

    test_run_time = round(time() - test_start_time, 4)
    if (correct_result == actual_result):
        print(f'{(colours.PASS + "Passed" + colours.ENDC):>10}', end=" ")
        print(test_run_time, "s")
        passed = passed + 1
    elif (type(correct_result) == Exception):
        print(f'{(colours.FAIL + "Failed" + colours.ENDC):>10}', end=" ")
        print(test_run_time, "s")
        print(actual_result)
        print("")
    else:
        print(f'{(colours.FAIL + "Failed" + colours.ENDC):>10}', end=" ")
        print(test_run_time, "s")
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
