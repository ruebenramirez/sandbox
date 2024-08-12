import click
from click.testing import CliRunner

from app import myadd, myadd_input_handler


def test_myadd(capfd):
    '''Test the myadd function directly.'''
    nums = (1, 2)
    myadd(nums)

    out, err = capfd.readouterr()

    assert '3' in out.strip()


def test_click_wrapper_around_myadd():
    '''Test the entire wrapper around the myadd function'''
    runner = CliRunner()
    result = runner.invoke(myadd_input_handler, ['101', '202'])
    assert result.exit_code == 0
    assert '303' in result.output


def test_error_on_too_many_parameters():
    '''test too many parameters provided (expect an error)'''
    runner = CliRunner()
    result = runner.invoke(myadd_input_handler, ['101', '202', '3'])
    expected_err_msg = "Error: Got unexpected extra argument (3)"
    assert expected_err_msg in result.output
    assert result.exit_code == 2


