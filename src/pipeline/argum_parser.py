import argparse


def parse_arguments() -> argparse.Namespace:
    """
    Parse arguments for init table or scrap
    :return:
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-act", "--action", help="Index of the start row.", type=str)

    parser.add_argument("-sR", "--start_row", help="Index of the start row.", type=int, default=0)
    parser.add_argument("-eR", "--end_row", help="Index of the end row.", type=int, default=20)
    parser.add_argument("-lB", "--length_batch", help="Length of the batch to analyze.", type=int, default=5)

    parser.add_argument("--version", action="version", version='%(prog)s - Version 1.0')

    args = parser.parse_args()

    return args
