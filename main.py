import argparse

from utils import compare_images


def main():
    parser = argparse.ArgumentParser(description="Compare two images.")
    parser.add_argument("image1", help="Path to first image")
    parser.add_argument("image2", help="Path to second image")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.99,
        help="Similarity threshold (default=0.99)",
    )
    parser.add_argument(
        "--save-diff", action="store_true", help="Save the difference image"
    )

    args = parser.parse_args()

    compare_images(args.image1, args.image2, threshold=args.threshold, save_diff=args.save_diff)


if __name__ == "__main__":
    main()
