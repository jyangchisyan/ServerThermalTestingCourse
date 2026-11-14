# 練習：逐段檢查相鄰資料

目前 `detect_by_rate` 只比較第一筆和最後一筆，因此看不到中途尖峰：

```python
temperature_spike = [
    ("10:03:00", 52, 61, 3100),
    ("10:03:10", 52, 78, 3100),
    ("10:03:20", 52, 61, 3100),
]
```

## 目標

逐段比較第 1 筆到第 2 筆，以及第 2 筆到第 3 筆。

```python
for index in range(len(temperature_spike) - 1):
    current_row = temperature_spike[index]
    next_row = temperature_spike[index + 1]

    # TODO：計算這一段經過幾秒
    # TODO：計算這一段每分鐘升溫多少度
    # TODO：印出 index 和升溫速度
```

## 執行前先預測

1. 迴圈會執行幾次？
2. 第一段每分鐘升溫多少度？
3. 第二段每分鐘溫度變化多少度？
4. 哪一段應觸發異常？

## 完成版本

完成後可執行根目錄的練習程式：

```bash
python3 exercise_adjacent.py
```
