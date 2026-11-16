"""示範距離、特徵縮放，以及簡化的 1-NN 分類。"""

from nearest_neighbor import (
    manhattan_distance,
    normalize_features,
    predict_1nn,
)


def main():
    # 階段一：只看升溫速度，正常案例會被誤判為異常。
    test_rate = 30.0
    normal_rate = 0.0
    abnormal_rate = 24.0
    print("單特徵距離正常：", abs(test_rate - normal_rate))
    print("單特徵距離異常：", abs(test_rate - abnormal_rate))

    # 階段二：原始尺度讓數值上千的風扇特徵主導距離。
    raw_test = (0, 24.0, 900)
    raw_normal = (0, 0.0, 1200)
    raw_abnormal = (0, 24.0, 0)
    print("原始距離正常：", manhattan_distance(raw_test, raw_normal))
    print("原始距離異常：", manhattan_distance(raw_test, raw_abnormal))

    # 階段三：縮放後，三種特徵的數值範圍較接近。
    test_features = normalize_features(raw_test)
    normal_features = normalize_features(raw_normal)
    abnormal_features = normalize_features(raw_abnormal)
    print("正規化距離正常：", manhattan_distance(test_features, normal_features))
    print("正規化距離異常：", manhattan_distance(test_features, abnormal_features))

    # 階段四：1-NN 使用最近訓練樣本的標籤。
    training_samples = [
        (normal_features, False),
        (abnormal_features, True),
    ]
    prediction, distance = predict_1nn(test_features, training_samples)
    print("風道受阻預測：", prediction, "距離：", distance)

    # 階段五：訓練案例太少，新的正常資料仍可能被誤判。
    new_normal = normalize_features((0, 0.0, 100))
    prediction, distance = predict_1nn(new_normal, training_samples)
    print("新正常資料預測：", prediction, "距離：", distance)


if __name__ == "__main__":
    main()
