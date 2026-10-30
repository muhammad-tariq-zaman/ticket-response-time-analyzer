"""Analyse first-response times from a ticket CSV (id,created,first_response).

Usage: python3 main.py tickets.csv --sla-hours 4
Timestamps must be ISO format, e.g. 2026-10-28T09:00:00.
"""
import argparse
import csv
import sys
from datetime import datetime


def response_hours(created, first):
    return (datetime.fromisoformat(first) - datetime.fromisoformat(created)).total_seconds() / 3600


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Ticket CSV file")
    parser.add_argument("--sla-hours", type=float, default=4.0)
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    hours = [response_hours(r["created"], r["first_response"]) for r in rows]
    breaches = sum(1 for h in hours if h > args.sla_hours)
    avg = sum(hours) / len(hours) if hours else 0
    print(f"{len(rows)} tickets, avg first response {avg:.2f}h, {breaches} breach(es) of {args.sla_hours:g}h SLA.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
