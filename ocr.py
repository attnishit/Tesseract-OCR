import argparse

import src.ocr


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file', help='path to image file you want to extract text from')

    args = parser.parse_args()

    src.ocr.main(args.file)


if __name__ == '__main__':
    main()
