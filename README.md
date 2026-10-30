# ticket-response-time-analyzer

Analyse first-response times from a ticket CSV and count breaches against an SLA in hours.

## How to run

```sh
python3 main.py tickets.csv --sla-hours 4
```

## Example output

```
3 tickets, avg first response 2.50h, 1 breach(es) of 4h SLA.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
