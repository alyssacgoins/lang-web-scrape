from processor import process
import argparse

# allowed source languages
# todo expand out
src_langs = ['DE']
# allowed target languages
# todo expand out
target_langs = ['EN']

""" Return URL from parsed command line arguments. """
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, help='Page to scrape')
    parser.add_argument('--src_lang', type=str, choices=src_langs,
                        help='Original page language')
    parser.add_argument('--target_lang', type=str,
                        choices=target_langs, help='Language to translate page')
    args = parser.parse_args()
    return args

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = parse_args()
    url = args.url
    src_lang = 'DE'
    target_lang = 'EN'

    # use target lang arg if specified. otherwise, default 'EN' used.
    if args.target_lang is not None:
        target_lang = args.target_lang
    # use src lang arg if specified. otherwise, default 'DE' used.
    if args.src_lang is not None:
        src_lang = args.src_lang
    process(url, src_lang)
