# Extraction Scoring Report

- Groundtruth dir: `E:\informationextract\evaluation\groundtruth`
- Output dir: `E:\informationextract\evaluation\output`
- Drop zero elements: `False`
- Value tolerance: `0.1`
- Temp tolerance (K): `1.0`
- Allow Celsius shift: `False`
- Ignore test unit: `False`
- Material match uses tests: `False`
- JSON report: `E:\informationextract\evaluation\scoring_report.json`

## Overall

### Composition Element Detection

- TP/FP/FN: `71` / `0` / `1`
- Precision/Recall/F1: `1.0000` / `0.9861` / `0.9930`

### Composition Value Error

- Count: `71`
- MAE: `1.936338`
- Max Abs Error: `52.42`
- Exact Rate: `0.549296`
- Within Tol Rate: `0.619718`

### Performance Test Detection

- TP/FP/FN: `6` / `3` / `0`
- Precision/Recall/F1: `0.6667` / `1.0000` / `0.8000`

### Performance Test Value Error

- Count: `6`
- MAE: `0.0`
- Max Abs Error: `0.0`
- Exact Rate: `1.0`
- Within Tol Rate: `1.0`

### Material-Level Full Hit

- Full Hit / Total: `10` / `11`
- Hit Rate: `0.909091`

## By Temperature (K)

| Temp_K | Test TP | Test FP | Test FN | Test F1 | Value Count | Value MAE | Value MaxErr |
|---:|---:|---:|---:|---:|---:|---:|---:|
| null | 0 | 3 | 0 | 0.0000 | 0 | None | None |
| 298.15 | 6 | 0 | 0 | 1.0000 | 6 | 0.0 | 0.0 |

## By Property Type

| Property | Test TP | Test FP | Test FN | Test F1 | Value Count | Value MAE | Value MaxErr |
|---|---:|---:|---:|---:|---:|---:|---:|
| microhardness | 6 | 0 | 0 | 1.0000 | 6 | 0.0 | 0.0 |
| relativedensity | 0 | 3 | 0 | 0.0000 | 0 | None | None |

## Per Article

### Article `AYzJ5YexzHG1b1fwF_ul`
- Composition Detection P/R/F1: `1.0000` / `0.9861` / `0.9930`
- Composition Value MAE: `1.936338` (count=71)
- Material Full Hit: `10/11` (hit_rate=0.909091)
- Test Detection P/R/F1: `0.6667` / `1.0000` / `0.8000`
- Test Value MAE: `0.0` (count=6)
