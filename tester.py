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
report_all_failures = False
report_failure_module = []
report_test_failure = False


def runTests(*tests):
    global total, passed, report_all_failures, report_failure_module, report_test_failure
    total = 0
    passed = 0
    if len(argv) > 1:
        if type(argv[1]) == str:
            if argv[1] == "all":
                report_all_failures = True
            else:
                try:
                    report_failure_module = [int(x) for x in argv[1]
                                             .replace("[", "")
                                             .replace("]", "")
                                             .split(',')]
                except:
                    print("Unrecognised arguement")
                    print("Accepted arguements:")
                    print("all - output all failure strings")
                    print("[x,y,z] - outputs failures for testgroup x,y,z")
                    quit()

    start_time = time()
    i = 0
    for test in tests:
        if report_all_failures:
            report_test_failure = True
        elif (report_failure_module.__contains__(i)):
            report_test_failure = True
        else:
            report_test_failure = False

        print(colours.HEADER + str(i) + ". " + test.__name__ + colours.ENDC)
        test()
        i += 1
    printResult(start_time)


def test(name, correct_result="NOT IMPLEMENTED", function=lambda x: x, *args, **kwargs):
    global total, passed, report_all_failures
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
        print(f'{(colours.PASS + "PASSED" + colours.ENDC):>10}', end=" ")
        print(test_run_time, "s")
        passed = passed + 1
    elif (type(correct_result) == Exception):
        print(f'{(colours.FAIL + "FAILED" + colours.ENDC):>10}', end=" ")
        print(test_run_time, "s")
        if report_test_failure:
            print(actual_result)
        print("")
    else:
        print(f'{(colours.FAIL + "FAILED" + colours.ENDC):>10}', end=" ")
        print(test_run_time, "s")
        if report_test_failure:
            print("Expected\n", correct_result, "\ngot\n", actual_result)


def printResult(start_time):
    global total, passed
    result = round(passed/total*100)

    if result == 100:
        status = colours.PASS
    else:
        status = colours.FAIL

    print(f'{(status + str(passed) + " out of " + str(total) + " tests passed in " + str(round((time() - start_time), 4)) + " seconds"):<50}' +
          f'{(str(result) + "%" + colours.ENDC):>14}')
