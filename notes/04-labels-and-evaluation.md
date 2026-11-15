# 第二課之一：標籤、預測與正確率

## 標籤是什麼

標籤（label）是人類提供的正確答案：

```text
False：正常
True：異常
```

一個有標籤的測試案例包含：

```python
(名稱, 感測資料, 正確標籤)
```

偵測器讀取感測資料後產生預測（prediction），再用 `prediction == expected` 檢查是否答對。

## 正確率

```text
Accuracy = 答對筆數 ÷ 總筆數
```

五筆熟悉資料全部答對時，Accuracy 是 100%。但這些資料曾參與規則設計，不能代表偵測器面對新資料也會一樣好。

## Accuracy 陷阱

假設十筆資料有九筆正常、一筆異常。偵測器永遠回答正常，仍會得到：

```text
Accuracy = 9 ÷ 10 = 90%
```

可是唯一的異常完全沒抓到。因此異常偵測不能只看 Accuracy。

對應程式：

```bash
python3 accuracy_trap.py
```
