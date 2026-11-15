"""示範只看 Accuracy 可能產生的誤解。"""

from evaluation import build_confusion_matrix, calculate_metrics, print_summary


def main():
    labels = [
        False, False, False, False, False,
        False, False, False, False, True,
    ]

    # 這個假偵測器永遠回答「正常」。
    predictions = [False] * len(labels)

    matrix = build_confusion_matrix(labels, predictions)
    metrics = calculate_metrics(matrix)
    print_summary(matrix, metrics)


if __name__ == "__main__":
    main()
