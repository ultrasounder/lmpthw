import argparse

parser = argparse.ArgumentParser(description='process some command line arguments')

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('-f', '--foo', help='foo help')
parser.add_argument('-b', '--bar', help='bar help')
parser.add_argument('-z', '--baz', help='baz help')
parser.add_argument('-t', '--turn-on', action='store_true')
parser.add_argument('-x', '--exclude', action='store_false')
parser.add_argument('-s', '--start', action='store_true')
args = parser.parse_args()


print(args.accumulate(args.integers))