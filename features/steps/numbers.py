from behave import when, then
from to_test.numbers import is_a_integer
from distutils.util import strtobool

@when('I check if a integer is a integer')
def step_impl(contex):
    contex.response = is_a_integer(1)

@when('I check if a float is a integer')
def step_impl(contex):
    contex.response = is_a_integer(1.1)

@then('It should return "{response}"')
def step_impl(contex, response):
    assert contex.response is bool(strtobool(response))