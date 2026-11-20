"""示範新增正常樣本、未見案例，以及 1-NN 的平手處理。"""

from nearest_neighbor import (
    normalize_features,
    predict_1nn,
    predict_1nn_with_ties,
)


def demonstrate_new_sample():
    """比較已加入訓練集的案例與相近的未見案例。"""
    training_samples = [
        (normalize_features((0, 0.0, 1200)), False),
        (normalize_features((0, 24.0, 0)), True),
    ]
    new_normal = normalize_features((0, 0.0, 100))
    training_samples.append((new_normal, False))

    prediction, distance = predict_1nn(new_normal, training_samples)
    print("已見案例預測：", prediction)
    print("最近距離：", distance)

    unseen_normal = normalize_features((0, 0.0, 120))
    prediction, distance = predict_1nn(unseen_normal, training_samples)
    print("未見案例預測：", prediction)
    print("最近距離：", round(distance, 4))


def demonstrate_ties():
    """比較原版和平手處理版對樣本排列順序的反應。"""
    samples = [
        ((0.0,), False),
        ((24.0,), True),
    ]
    test_features = (12.0,)

    print("原版，原順序：", predict_1nn(test_features, samples))
    print("原版，反轉順序：", predict_1nn(test_features, samples[::-1]))
    print("平手版，原順序：", predict_1nn_with_ties(test_features, samples))
    print("平手版，反轉順序：", predict_1nn_with_ties(test_features, samples[::-1]))


def main():
    demonstrate_new_sample()
    print()
    demonstrate_ties()


if __name__ == "__main__":
    main()
