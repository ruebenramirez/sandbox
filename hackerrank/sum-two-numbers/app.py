import click

from typing import Tuple


def myadd(nums: Tuple[int, ...]):
    '''Add two provided numbers together and print the result.

    Separate logic from the input handling to improve testability.'''
    mysum = 0
    for num in nums:
        mysum += num
    return mysum


@click.command()
@click.argument('nums', nargs=2, type=int)
def myadd_io_handler(nums: Tuple[int, ...]):
    '''Grab input of 2 numbers and forward them along to our myadd logic.

    Print the calculated total.'''
    mysum = myadd(nums)
    click.echo(mysum)


if __name__ == '__main__':
    myadd_io_handler()
