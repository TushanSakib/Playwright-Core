import pytest_check as check
from pytest_check import is_false


class SoftAssert:
    @staticmethod
    def verify_equal(
            actual,
            expected,
            message=""
    ):
        check.equal(actual, expected, message)

    @staticmethod
    def verify_true(condition,message):
        check.is_true(condition,message)

    @staticmethod
    def verify_false(condition,message):
        check.is_false(condition,message)