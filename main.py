from processor import process
import argparse

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


""" Return URL from parsed command line arguments. """
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    args = parser.parse_args()
    return args.url

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = parse_args()
    process(url)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
