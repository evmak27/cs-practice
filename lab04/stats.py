def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Ожидалось 3 поля")
    city, temp_str, date = parts
    if not city or not date:
        raise ValueError("Пустой город или дата")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Температура не является числом")
    return {"city": city, "temp": temp, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    sums = {}
    counts = {}
    for r in records:
        city = r["city"]
        sums[city] = sums.get(city, 0) + r["temp"]
        counts[city] = counts.get(city, 0) + 1
    return {city: round(sums[city] / counts[city], 1) for city in sums}

def warmest_city(records: list[dict]) -> str:
    avg_dict = average_by_city(records)
    if not avg_dict:
        return ""
    return sorted(avg_dict.items(), key=lambda item: (-item[1], item[0]))[0][0]