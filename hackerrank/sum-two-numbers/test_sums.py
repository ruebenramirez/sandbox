import click
from click.testing import CliRunner
import pytest

from app import myadd, myadd_io_handler


def test_myadd():
    '''Test the myadd function directly.

    - The calculation function takes a parameter of a set of inputs.
    '''
    nums = (1, 2)
    total = myadd(nums)
    assert total == 3


def test_myadd_bad_input():
    with pytest.raises(TypeError) as excinfo:
        bad_nums = ('r', 'u')
        myadd(bad_nums)


def test_click_wrapper_around_myadd():
    '''Behavioral end to end test.


    - Initiate the test harness for the cli app.
    - Execute the app with the appropriate input arguments.
    - Confirm the correct total is calculated.
    '''
    runner = CliRunner()
    result = runner.invoke(myadd_io_handler, ['101', '202'])
    assert result.exit_code == 0
    assert '303' in result.output


def test_error_on_too_many_parameters():
    '''Test too many parameters provided (expect an error).

    - The app takes two numbers as inputs.
    - If more inputs are provided, the app should error out.
    '''
    runner = CliRunner()
    result = runner.invoke(myadd_io_handler, ['101', '202', '303'])

    expected_err_msg = "Error: Got unexpected extra argument (303)"
    assert expected_err_msg in result.output
    assert result.exit_code == 2


