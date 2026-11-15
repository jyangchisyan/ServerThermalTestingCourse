"""計算分類結果的混淆矩陣與常用評估指標。"""


def build_confusion_matrix(labels, predictions):
    """回傳 TP、TN、FP、FN 四個計數。"""
    matrix = {"tp": 0, "tn": 0, "fp": 0, "fn": 0}

    for expected, prediction in zip(labels, predictions):
        if expected and prediction:
            matrix["tp"] += 1
        elif not expected and not prediction:
            matrix["tn"] += 1
        elif not expected and prediction:
            matrix["fp"] += 1
        else:
            matrix["fn"] += 1

    return matrix


def percentage(numerator, denominator):
    """安全地計算百分比，避免除以零。"""
    if denominator == 0:
        return 0.0
    return numerator / denominator * 100


def calculate_metrics(matrix):
    """從混淆矩陣計算 accuracy、precision 與 recall。"""
    tp = matrix["tp"]
    tn = matrix["tn"]
    fp = matrix["fp"]
    fn = matrix["fn"]
    total = tp + tn + fp + fn

    return {
        "accuracy": percentage(tp + tn, total),
        "precision": percentage(tp, tp + fp),
        "recall": percentage(tp, tp + fn),
    }


def print_summary(matrix, metrics):
    """用一致格式印出混淆矩陣與指標。"""
    print("異常抓對 TP：", matrix["tp"])
    print("正常判對 TN：", matrix["tn"])
    print("誤報 FP：", matrix["fp"])
    print("漏報 FN：", matrix["fn"])
    print("正確率 Accuracy：", round(metrics["accuracy"], 2), "%")
    print("異常精確率 Precision：", round(metrics["precision"], 2), "%")
    print("異常召回率 Recall：", round(metrics["recall"], 2), "%")
