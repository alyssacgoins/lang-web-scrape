from processor import Processor
from retriever import Retriever
from src.cleaner import Cleaner
import argparse


""" Return URL from parsed command line arguments. """
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, required=True,
                        help='Page to scrape')
    parser.add_argument('--src_lang', type=str,
                        choices=['DE'],
                        help='Original page language')
    parser.add_argument('--target_lang', type=str,
                        choices=['EN'],
                        help='Language to translate page')
    input_args = parser.parse_args()
    return input_args

""" Program driver """
if __name__ == '__main__':
    args = parse_args()
    url = args.url
    src_lang = 'DE'
    target_lang = 'EN'

    # use target lang arg if specified. otherwise, default 'EN' used.
    if args.target_lang is not None:
        src_lang = args.target_lang
    # use src lang arg if specified. otherwise, default 'DE' used.
    if args.src_lang is not None:
        target_lang = args.src_lang

    # instantiate retriever, processor & cleaner
    retriever = Retriever(url)
    processor = Processor(Cleaner(src_lang, target_lang))

    # retrieve body text
    retrieved = retriever.retrieve_body_text()
    # clean retrieved text and save to csv
    processor.process_body_text(retrieved)
