import re
import pytest
import task_12_3
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, ping, get_reach_unreach

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def unified_columns_output(output):
    lines = [re.split(r"  +", line.strip()) for line in output.strip().split("\n")]
    formatted = [("{:25}"*len(line)).format(*line) for line in lines]
    return "\n".join(formatted)


def test_function_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_12_3, "print_ip_table")


def test_function_stdout(capsys):
    """
    Task check
    """
    reach_ip = ["10.10.1.7", "10.10.1.8", "10.10.1.9", "10.10.1.15"]
    unreach_ip = ["10.10.2.1", "10.10.1.2"]
    return_value = task_12_3.print_ip_table(reach_ip, unreach_ip)

    stdout, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "Reachable    Unreachable\n"
        "-----------  -------------\n"
        "10.10.1.7    10.10.2.1\n"
        "10.10.1.8    10.10.1.2\n"
        "10.10.1.9\n"
        "10.10.1.15\n"
    )
    assert return_value == None, "The function must return None"
    assert (
        unified_columns_output(stdout) == correct_stdout
    ), "Function returns wrong value"
