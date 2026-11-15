"""示範特徵提取、樣本建立，以及訓練/測試切分。"""

from cooling_data import NORMAL_FAN_CATCHUP, generate_abnormal
from feature_engineering import extract_features, make_samples, split_samples


def labels_from(samples):
    """取出樣本中的標籤，方便觀察切分結果。"""
    return [sample[1] for sample in samples]


def main():
    first_features = extract_features(
        NORMAL_FAN_CATCHUP[0],
        NORMAL_FAN_CATCHUP[1],
    )
    print("第一段特徵：", first_features)

    normal_samples = make_samples(NORMAL_FAN_CATCHUP, False)
    abnormal_samples = make_samples(generate_abnormal(), True)
    all_samples = normal_samples + abnormal_samples

    print("正常樣本：", normal_samples)
    print("異常樣本：", abnormal_samples)
    print("樣本總數：", len(all_samples))

    train_samples, test_samples = split_samples(
        all_samples,
        train_size=3,
        seed=42,
    )

    print("訓練標籤：", labels_from(train_samples))
    print("測試標籤：", labels_from(test_samples))


if __name__ == "__main__":
    main()
