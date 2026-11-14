# 簡化伺服器散熱異常偵測器

這是從零開始的深度學習實作課程第一課。目前還沒有使用深度學習；我們先用 Python 標準函式庫理解資料、規則、誤報與漏報。

## 執行

```bash
python3 run_time.py
```

## 檔案導覽

- `cooling_data.py`：產生資料與保存測試情境。
- `cooling_detectors.py`：三版異常偵測規則。
- `run_time.py`：執行所有情境並比較結果。
- `notes/01-data-and-python.md`：資料格式與 Python 基礎。
- `notes/02-detection-rules.md`：三版規則與改良原因。
- `notes/03-errors-and-lessons.md`：實作中遇到的錯誤與重點。
- `exercises/01-adjacent-windows.md`：下一個練習，不先提供答案。

## 目前結論

單看溫度容易誤報；只比較頭尾又可能漏掉中途尖峰。較好的偵測方式需要同時考慮 CPU 負載、溫度隨時間的變化，以及風扇是否有效控制溫度。
