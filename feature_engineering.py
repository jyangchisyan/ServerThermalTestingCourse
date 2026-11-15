"""把原始感測資料轉成可供模型使用的特徵與樣本。"""

from random import Random

from cooling_detectors import calculate_rise_per_minute


def extract_features(current_row, next_row):
    """從兩筆相鄰資料提取 CPU、溫度與風扇變化。"""
    cpu_change = abs(next_row[1] - current_row[1])
    temperature_rate = calculate_rise_per_minute(current_row, next_row)
    fan_change = next_row[3] - current_row[3]

    return (cpu_change, temperature_rate, fan_change)


def make_samples(data, label):
    """把一段資料轉成多個（特徵向量, 標籤）樣本。"""
    samples = []

    for index in range(len(data) - 1):
        current_row = data[index]
        next_row = data[index + 1]
        features = extract_features(current_row, next_row)
        samples.append((features, label))

    return samples


def split_samples(samples, train_size, seed=42):
    """複製並打亂樣本，再切成訓練集與測試集。"""
    if train_size < 0 or train_size > len(samples):
        raise ValueError("train_size 必須介於 0 與樣本總數之間")

    shuffled_samples = samples.copy()
    random_generator = Random(seed)
    random_generator.shuffle(shuffled_samples)

    train_samples = shuffled_samples[:train_size]
    test_samples = shuffled_samples[train_size:]
    return train_samples, test_samples
