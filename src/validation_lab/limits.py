def check_temperature(celsius: float, max_celsius: float = 100.0) -> str:
    """Return 'ok', 'warning' or 'fail' for a temperature reading."""
    if celsius < -50 or celsius > 200:
        raise ValueError(f"Reading out of sensor range: {celsius}")
    if celsius > max_celsius:
        return "fail"
    if celsius > max_celsius * 0.9:
        return "warning"
    return "ok"
