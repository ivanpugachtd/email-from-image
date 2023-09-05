import argparse


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Extract email addresses from an image."
        )
        self.parser.add_argument(
            "--input", type=str, required=True, help="Path to the image file."
        )
        self.parser.add_argument(
            "--output",
            type=str,
            required=True,
            help="Path to the output text file to store extracted emails.",
        )

    def get_args(self):
        return self.parser.parse_args()
