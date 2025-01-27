from processor import process
import argparse
from cleaner import set_src_lang, set_target_lang


# allowed source languages
# todo expand out
src_lang_options = ['DE']
# allowed target languages
# todo expand out
target_lang_options = ['EN']

""" Return URL from parsed command line arguments. """
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, help='Page to scrape')
    parser.add_argument('--src_lang', type=str, choices=src_lang_options,
                        help='Original page language')
    parser.add_argument('--target_lang', type=str,
                        choices=target_lang_options, help='Language to translate page')
    args = parser.parse_args()
    return args

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = parse_args()
    url = args.url

    # use target lang arg if specified. otherwise, default 'EN' used.
    if args.target_lang is not None:
        set_target_lang(args.target_lang)
    # use src lang arg if specified. otherwise, default 'DE' used.
    if args.src_lang is not None:
        set_src_lang(args.src_lang)
    process(url)
