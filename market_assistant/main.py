"""Market assistant entry point."""
import argparse

from reports.daily_report import generate_daily_report


def main():
    parser = argparse.ArgumentParser(description="Run market assistant")
    parser.add_argument('mode', choices=['daily'], help="Execution mode")
    args = parser.parse_args()

    if args.mode == 'daily':
        generate_daily_report()


if __name__ == '__main__':
    main()
