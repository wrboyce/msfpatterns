import argparse

from . import generate_pattern, find_offset


def main() -> None:
    """CLI interface for pattern generation and offset searching."""
    parser = argparse.ArgumentParser(
        description="Cyclic pattern generator & offset finder (Metasploit style)"
    )
    parser.add_argument(
        "length", type=int, help="Length of the pattern to generate/search"
    )
    parser.add_argument(
        "-q",
        "--query",
        metavar="VALUE",
        type=str,
        help="Find offset of VALUE inside a pattern",
    )
    args = parser.parse_args()

    if args.query:
        try:
            offsets = find_offset(args.query, args.length)
            if offsets is not None:
                match_count = len(offsets)
                if match_count > 1:
                    print(
                        f"[*] Found {match_count} occurrences at offsets: {', '.join(map(str, offsets))}"
                    )
                else:
                    print(f"[*] Found 1 occurrence at offset: {offsets[0]}")
            else:
                print("[x] Value not found in the pattern.")
        except ValueError as e:
            print(f"[x] {e}")
            exit(1)
    else:
        print(generate_pattern(args.length))


if __name__ == "__main__":
    main()
