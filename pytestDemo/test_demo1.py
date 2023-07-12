# Any pytest file should start with test_
import py
import pytest


# Write the code in the function in the pytest

# Pytest test method should start with test
# Any method should wrapped in method only
# Each every method consider as one method
# Run through test runner
# -----------------------------------------------------------------------------------------------------
# To run tests in pycharm then ctrl+shit+f10
# Run test in cmd
# -------------------------------------------------------------------------------------------------------
# To run test through command promt the we need to copy path of python package, type cd path paste +click enter
# Click py.test +enter
# To see complete information then type py.test -v+enter
# To print all console logs then py.test -v -s+enter
# To run entire python package the py.test -v -s then all methods excute
# To run python package and file  then "py.test file name  -v -s"
# To run particular method or test case then "py.test -k method name  -v -s"
# to run particular test (ex: smoke testing) at time method called mark "py.test -m mark smoke -v -s"
# py.test.mark.smoke
# To skip test case at that time will use skip
# "py.test.mark.skip" need to mention at that test case.
# "py.test.mark.xfail" these annotation will used for it will run but does not show any output for particular testcase.
# fixures are used to execute the before (Need to use "setup" keyword ), after executing setup argument fixtures are execute.
# "yield" is used to execute once completion of fixtures execution
# need to create file conftest which are used to common test cases and will add fixtures and we will call argument by calling key word setup.
# (Place scope = "class") in the fixtures contest file then it execute once in a class not each and every method.
# fixtures not only help  to execute pre request and also help to load data (Data should ready  before doing test).
# Data driven and parameterization can be done  with return statements in tuple format
# when you define fixtures scope to class only , it will run once before class is initiated and at the end.








@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


def test_secondProgram():
        print("Good Morning")


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixturesDemo(self):
        print("i will execute fixtures demo method")

    def test_fixturesDemo1(self):
        print("i will execute fixtures demo1 method")

    def test_fixturesDemo2(self):
        print("i will execute fixtures demo2 method")
    def test_fixturesDemo3(self):
        print("i will execute fixtures demo3 method")
    def test_fixturesDemo4(self):
        print("i will execute fixtures demo4 method")


def test_crossBrowser(crossBrowser):
        print(crossBrowser)
