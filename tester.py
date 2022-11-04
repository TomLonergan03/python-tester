from sys import argv

class colours:
    PASS = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

total = 0
passed = 0

def run(*tests):
    global total, passed
    total = 0
    passed = 0  
    for test in tests:
        test()
    printResult()

def assertEqual(name, correct_result, function = lambda x:x, *args):
    global total, passed
    total = total + 1
    testname = "Test " + str(total) + ": " + str(name)
    print(f"{testname:<50}", sep="",end=" ")
    actual_result = function(*args)
    if (correct_result == actual_result):
        print(f'{(colours.PASS + "Passed" + colours.ENDC):>10}')
        passed = passed + 1
    else:
        print(colours.FAIL + "Failed" + colours.ENDC)
        print("Expected", correct_result, "got", actual_result)

def printResult():
    global total, passed
    result = round(passed/total*100)

    if result == 100:
        print(f'{(colours.PASS + str(passed) + " out of " + str(total) + " total tests"):<50}' + f'{(str(result) + "%" + colours.ENDC):>14}')
    else:
        print(f'{(colours.FAIL + str(passed) + " out of " + str(total) + " total tests"):<50}' + f'{(str(result) + "%" + colours.ENDC):>14}')