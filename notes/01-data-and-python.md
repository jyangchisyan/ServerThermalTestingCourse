# 第一課之一：資料與 Python 基礎

每筆資料是一個 tuple，欄位順序固定：

```python
(時間, CPU 負載, 溫度, 風扇轉速)
```

例如：

```python
("10:00:10", 54, 56.2, 2820)
```

## 本課使用的 Python 觀念

- `range(3)` 產生 `0、1、2`，不是 `1、2、3`。
- 3 個資料點之間只有 2 個時間間隔。
- `data[0]` 是第一筆，`data[-1]` 是最後一筆。
- `enumerate` 可以同時取得編號和內容。
- `append` 把一筆資料加入 list。
- `return` 要放在迴圈外，否則函式第一圈就會結束。
- tuple 可以拆解成 `time_text, cpu, temperature, fan_rpm`。
- `datetime.strptime` 把時間文字轉成可計算的時間。

## 正常與異常的核心差異

正常情境：

```text
CPU 上升 → 溫度上升 → 風扇加速
```

異常情境：

```text
CPU 穩定 → 溫度持續上升 → 風扇沒有加速或散熱沒有效果
```
