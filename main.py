from processor import process
import argparse

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
