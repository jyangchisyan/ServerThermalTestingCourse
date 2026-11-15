# 第二課之二：混淆矩陣與評估指標

## 四種結果

| 名稱 | 實際情況 | 預測結果 | 意義 |
|---|---|---|---|
| TP | 異常 | 異常 | 成功抓到異常 |
| TN | 正常 | 正常 | 成功判斷正常 |
| FP | 正常 | 異常 | 誤報 |
| FN | 異常 | 正常 | 漏報 |

四格總和應等於資料總數：

```text
TP + TN + FP + FN = 總筆數
```

## Accuracy

所有資料中答對的比例：

```text
Accuracy = (TP + TN) ÷ (TP + TN + FP + FN)
```

## Precision

所有異常警報中，有多少是真的：

```text
Precision = TP ÷ (TP + FP)
```

Precision 低代表誤報多，可能讓管理員逐漸忽略警報。

## Recall

所有真正異常中，成功抓到多少：

```text
Recall = TP ÷ (TP + FN)
```

Recall 低代表漏報多。對硬體過熱等安全情境，漏報通常代價很高。

## 除以零

如果偵測器從未發出異常警報，`TP + FP` 會是 0。教學程式使用 `percentage()` 避免 `ZeroDivisionError`，並把結果設為 0。

共用程式位於 `evaluation.py`。
