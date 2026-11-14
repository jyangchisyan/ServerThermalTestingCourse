"""四種逐步改良的散熱異常偵測規則。"""

from datetime import datetime


def detect_by_temperature(data, threshold=65):
    """第一版：任一筆溫度超過門檻，就判定異常。"""
    for time_text, cpu, temperature, fan_rpm in data:
        if temperature > threshold:
            return True
    return False


def detect_by_trend(data):
    """第二版：比較第一筆和最後一筆的 CPU、溫度及風扇。"""
    if len(data) < 2:
        return False

    first = data[0]
    last = data[-1]
    cpu_change = abs(last[1] - first[1])
    temperature_rise = last[2] - first[2]
    fan_change = last[3] - first[3]

    cpu_stable = cpu_change <= 5
    temperature_rising = temperature_rise >= 6
    fan_not_speeding_up = fan_change <= 200
    return cpu_stable and temperature_rising and fan_not_speeding_up


def calculate_rise_per_minute(first, last):
    """計算兩筆資料之間每分鐘升溫多少度。"""
    start_time = datetime.strptime(first[0], "%H:%M:%S")
    end_time = datetime.strptime(last[0], "%H:%M:%S")
    elapsed_seconds = (end_time - start_time).total_seconds()

    if elapsed_seconds <= 0:
        return 0

    temperature_rise = last[2] - first[2]
    return temperature_rise / elapsed_seconds * 60


def detect_by_rate(data, rate_limit=18):
    """第三版：CPU 穩定且溫度快速上升時判定異常。"""
    if len(data) < 2:
        return False

    first = data[0]
    last = data[-1]
    cpu_change = abs(last[1] - first[1])
    rise_per_minute = calculate_rise_per_minute(first, last)

    cpu_stable = cpu_change <= 5
    temperature_rising_fast = rise_per_minute >= rate_limit
    return cpu_stable and temperature_rising_fast


def detect_by_window_rate(data, rate_limit=20):
    """第四版：逐段檢查 CPU 是否穩定且溫度快速上升。"""
    if len(data) < 2:
        return False

    for index in range(len(data) - 1):
        current_row = data[index]
        next_row = data[index + 1]

        cpu_change = abs(next_row[1] - current_row[1])
        rise_per_minute = calculate_rise_per_minute(
            current_row,
            next_row,
        )

        cpu_stable = cpu_change <= 5
        temperature_rising_fast = rise_per_minute >= rate_limit

        if cpu_stable and temperature_rising_fast:
            return True

    return False
