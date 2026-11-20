"""只使用 Python 標準函式庫實作簡化的 1-NN 分類器。"""

from math import isclose

CPU_SCALE = 100
TEMPERATURE_RATE_SCALE = 30
FAN_CHANGE_SCALE = 1200


def normalize_features(features):
    """使用教學用尺度，把三個特徵縮放到接近 0～1。"""
    cpu_change, temperature_rate, fan_change = features

    return (
        cpu_change / CPU_SCALE,
        temperature_rate / TEMPERATURE_RATE_SCALE,
        fan_change / FAN_CHANGE_SCALE,
    )


def manhattan_distance(features_a, features_b):
    """計算兩個同長度特徵向量的曼哈頓距離。"""
    if len(features_a) != len(features_b):
        raise ValueError("兩個特徵向量的長度必須相同")

    distance = 0
    for index in range(len(features_a)):
        distance += abs(features_a[index] - features_b[index])

    return distance


def predict_1nn(test_features, training_samples):
    """回傳距離最近之訓練樣本的標籤與距離。"""
    if not training_samples:
        raise ValueError("訓練樣本不能是空的")

    nearest_distance = float("inf")
    nearest_label = None

    for known_features, known_label in training_samples:
        distance = manhattan_distance(test_features, known_features)

        if distance < nearest_distance:
            nearest_distance = distance
            nearest_label = known_label

    return nearest_label, nearest_distance


def predict_1nn_with_ties(test_features, training_samples):
    """最近樣本標籤衝突時回傳 None，否則回傳一致的標籤。"""
    if not training_samples:
        raise ValueError("訓練樣本不能是空的")

    distances = []
    for features, label in training_samples:
        distance = manhattan_distance(test_features, features)
        distances.append((distance, label))

    nearest_distance = min(distance for distance, label in distances)
    nearest_labels = set()

    for distance, label in distances:
        if isclose(distance, nearest_distance, rel_tol=1e-9, abs_tol=1e-12):
            nearest_labels.add(label)

    if len(nearest_labels) > 1:
        return None, nearest_distance

    return nearest_labels.pop(), nearest_distance
