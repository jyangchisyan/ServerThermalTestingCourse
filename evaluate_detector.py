"""用有標籤的情境評估第四版散熱偵測器。"""

from cooling_data import (
    BLOCKED_AIRFLOW,
    HOT_BUT_NORMAL,
    NORMAL_FAN_CATCHUP,
    TEMPERATURE_SPIKE,
    generate_abnormal,
    generate_normal,
)
from cooling_detectors import detect_by_window_rate
from evaluation import build_confusion_matrix, calculate_metrics, print_summary


def main():
    labeled_cases = [
        ("一般正常", generate_normal(), False),
        ("散熱異常", generate_abnormal(), True),
        ("高負載正常", HOT_BUT_NORMAL, False),
        ("風道堵塞", BLOCKED_AIRFLOW, True),
        ("中途溫度暴升", TEMPERATURE_SPIKE, True),
        ("風扇追上正常", NORMAL_FAN_CATCHUP, False),
    ]

    labels = []
    predictions = []

    for name, data, expected in labeled_cases:
        prediction = detect_by_window_rate(data)
        labels.append(expected)
        predictions.append(prediction)

        print(
            name,
            "標籤：", expected,
            "預測：", prediction,
            "答對：", prediction == expected,
        )

    print()
    matrix = build_confusion_matrix(labels, predictions)
    metrics = calculate_metrics(matrix)
    print_summary(matrix, metrics)


if __name__ == "__main__":
    main()
