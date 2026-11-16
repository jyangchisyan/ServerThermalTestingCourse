# 簡化伺服器散熱異常偵測器

這是從零開始的深度學習實作課程第一課。目前還沒有使用深度學習；我們先用 Python 標準函式庫理解資料、規則、誤報與漏報。

## 執行

```bash
# 比較四版規則
python3 run_time.py

# 逐段升溫速度練習
python3 exercise_adjacent.py

# 觀察 Accuracy 陷阱
python3 accuracy_trap.py

# 評估第四版偵測器
python3 evaluate_detector.py

# 特徵提取與訓練/測試切分
python3 feature_practice.py

# 距離、正規化與第一個 1-NN 分類器
python3 nearest_neighbor_practice.py
```

## 檔案導覽

- `cooling_data.py`：產生資料與保存測試情境。
- `cooling_detectors.py`：四版異常偵測規則。
- `evaluation.py`：共用的混淆矩陣與評估指標函式。
- `feature_engineering.py`：特徵提取、樣本建立與資料切分。
- `nearest_neighbor.py`：曼哈頓距離、特徵正規化與 1-NN 分類器。
- `run_time.py`：執行所有情境並比較結果。
- `exercise_adjacent.py`：逐段升溫速度練習的完成版本。
- `accuracy_trap.py`：示範 90% Accuracy 仍可能漏掉全部異常。
- `evaluate_detector.py`：用標籤、混淆矩陣及指標評估第四版。
- `feature_practice.py`：從原始資料建立帶標籤樣本並切分資料。
- `nearest_neighbor_practice.py`：1-NN 的分階段實作與失敗案例。
- `notes/01-data-and-python.md`：資料格式與 Python 基礎。
- `notes/02-detection-rules.md`：四版規則與改良原因。
- `notes/03-errors-and-lessons.md`：實作中遇到的錯誤與重點。
- `notes/04-labels-and-evaluation.md`：標籤、預測與正確率。
- `notes/05-confusion-matrix-and-metrics.md`：TP、TN、FP、FN 與三個指標。
- `notes/06-unseen-data.md`：未見資料、泛化與目前規則的缺陷。
- `notes/07-feature-engineering.md`：原始資料、特徵向量與訓練樣本。
- `notes/08-train-test-split.md`：打亂、亂數種子與訓練/測試切分。
- `notes/09-distance-and-nearest-neighbor.md`：距離與最近鄰概念。
- `notes/10-feature-scaling.md`：不同特徵尺度造成的偏差。
- `notes/11-first-1nn-classifier.md`：第一個分類器與訓練資料覆蓋。
- `exercises/01-adjacent-windows.md`：下一個練習，不先提供答案。

## 目前結論

單看溫度容易誤報；只比較頭尾又可能漏掉中途尖峰。第四版能抓到中途暴升，但在「風扇稍慢後追上」的新資料上仍會誤報。這正是後續需要更多資料、特徵與機器學習方法的原因。
