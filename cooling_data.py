"""伺服器散熱教學使用的模擬資料。"""

from datetime import datetime, timedelta


def generate_normal():
    """產生 CPU 負載升高、風扇正常加速的資料。"""
    start = datetime(2026, 11, 14, 10, 0, 0)
    cpu_loads = [35, 54, 76]
    data = []

    for step, cpu in enumerate(cpu_loads):
        current = start + timedelta(seconds=step * 10)
        temperature = round(40 + cpu * 0.3, 1)
        fan_rpm = round(1200 + (temperature - 40) * 100)
        time_text = current.strftime("%H:%M:%S")
        data.append((time_text, cpu, temperature, fan_rpm))

    return data


def generate_abnormal():
    """產生負載穩定、溫度上升、風扇不加速的資料。"""
    start = datetime(2026, 11, 14, 10, 0, 0)
    data = []

    for step in range(3):
        current = start + timedelta(seconds=step * 10)
        time_text = current.strftime("%H:%M:%S")
        data.append((time_text, 52, 61 + step * 4, 3100))

    return data


HOT_BUT_NORMAL = [
    ("10:01:00", 76, 59, 3900),
    ("10:01:10", 91, 66, 5100),
    ("10:01:20", 94, 69, 5600),
]

BLOCKED_AIRFLOW = [
    ("10:02:00", 52, 61, 3100),
    ("10:02:10", 52, 66, 3400),
    ("10:02:20", 52, 71, 3700),
]

TEMPERATURE_SPIKE = [
    ("10:03:00", 52, 61, 3100),
    ("10:03:10", 52, 78, 3100),
    ("10:03:20", 52, 61, 3100),
]

NORMAL_FAN_CATCHUP = [
    ("10:04:00", 50, 60, 3000),
    ("10:04:10", 50, 65, 4200),
    ("10:04:20", 50, 65, 4300),
]
