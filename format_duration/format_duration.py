def format_duration(seconds):
    if not seconds:
        return "now"

    conversions = {
        ("minutes", "seconds"): 60,
        ("hours", "minutes"): 60,
        ("days", "hours"): 24,
        ("years", "days"): 365
    }
    periods = {"seconds": seconds}

    for (to_period, from_period), rate in conversions.items():
        periods[to_period] = periods[from_period] // rate
        periods[from_period] %= rate

    periods_list = [f"{val} {name if val > 1 else name[:-1]}" for name,
                    val in periods.items() if val][::-1]

    if len(periods_list) == 1:
        return periods_list[0]
    return ", ".join(periods_list[:-1]) + " and " + periods_list[-1]
