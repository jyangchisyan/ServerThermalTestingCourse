"""執行所有散熱情境，並比較四版偵測規則。"""

from cooling_data import (
    BLOCKED_AIRFLOW,
    HOT_BUT_NORMAL,
    TEMPERATURE_SPIKE,
    generate_abnormal,
    generate_normal,
)
from cooling_detectors import (
    detect_by_rate,
    detect_by_temperature,
    detect_by_trend,
    detect_by_window_rate,
)


def print_data(title, data):
    print(f"\n{title}")
    print("時間      CPU  溫度  風扇")
    for time_text, cpu, temperature, fan_rpm in data:
        print(time_text, cpu, temperature, fan_rpm)


def print_results(data):
    print("溫度門檻規則：", detect_by_temperature(data))
    print("頭尾趨勢規則：", detect_by_trend(data))
    print("升溫速度規則：", detect_by_rate(data))
    print("逐段速度規則：", detect_by_window_rate(data))


def main():
    test_cases = [
        ("一般正常資料", generate_normal()),
        ("散熱異常資料", generate_abnormal()),
        ("高負載正常資料", HOT_BUT_NORMAL),
        ("風道堵塞", BLOCKED_AIRFLOW),
        ("中途溫度暴升", TEMPERATURE_SPIKE),
    ]

    for title, data in test_cases:
        print_data(title, data)
        print_results(data)

if __name__ == "__main__":
    main()
