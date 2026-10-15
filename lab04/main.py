import sys
from stats import read_valid, average_by_city, warmest_city

lines = sys.stdin.read().splitlines()
records = read_valid(lines)

parsed_count = len(records)
skipped_count = len([l for l in lines if l.strip()]) - parsed_count

print(parsed_count)
print(skipped_count)

if records:
    avg_dict = average_by_city(records)
    best = warmest_city(records)
    print(f"{avg_dict[best]:.1f}")
else:
    print(0.0)