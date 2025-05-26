import csv
from collections import defaultdict
from multiprocessing import Pool, cpu_count

def mapper(record):
    """
    Simulates the Map step: returns (passenger_id, 1) for a single record.
    """
    try:
        fields = record.strip().split(",")
        passenger_id = fields[0]
        return (passenger_id, 1)
    except IndexError:
        return None

