# Extraction Scoring Report

- Groundtruth dir: `groundtruth`
- Output dir: `output`
- Drop zero elements: `False`
- Value tolerance: `0.1`
- Temp tolerance (K): `1.0`
- Allow Celsius shift: `False`
- Ignore test unit: `False`
- Material match uses tests: `False`
- JSON report: `/Users/zhangziyu02/Desktop/对比试验/scoring_report.json`

## Overall

### Composition Element Detection

- TP/FP/FN: `55` / `1` / `1`
- Precision/Recall/F1: `0.9821` / `0.9821` / `0.9821`

### Composition Value Error

- Count: `55`
- MAE: `2.152303`
- Max Abs Error: `58.991544`
- Exact Rate: `0.672727`
- Within Tol Rate: `0.854545`

### Performance Test Detection

- TP/FP/FN: `86` / `18` / `32`
- Precision/Recall/F1: `0.8269` / `0.7288` / `0.7748`

### Performance Test Value Error

- Count: `86`
- MAE: `25.838372`
- Max Abs Error: `415.5`
- Exact Rate: `0.802326`
- Within Tol Rate: `0.813953`

## By Temperature (K)

| Temp_K | Test TP | Test FP | Test FN | Test F1 | Value Count | Value MAE | Value MaxErr |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 77 | 4 | 2 | 2 | 0.6667 | 4 | 0.0 | 0.0 |
| 298 | 30 | 2 | 14 | 0.7895 | 30 | 0.0 | 0.0 |
| 673 | 2 | 0 | 0 | 1.0000 | 2 | 0.0 | 0.0 |
| 773 | 4 | 1 | 1 | 0.8000 | 4 | 0.0 | 0.0 |
| 873 | 13 | 2 | 13 | 0.6341 | 13 | 83.861538 | 415.5 |
| 973 | 5 | 1 | 0 | 0.9091 | 5 | 143.54 | 260.0 |
| 1073 | 6 | 0 | 0 | 1.0000 | 6 | 35.7 | 77.0 |
| 1173 | 8 | 0 | 0 | 1.0000 | 8 | 0.0 | 0.0 |
| 1273 | 4 | 2 | 0 | 0.8000 | 4 | 0.0 | 0.0 |
| 1473 | 4 | 2 | 2 | 0.6667 | 4 | 0.0 | 0.0 |
| 1673 | 2 | 4 | 0 | 0.5000 | 2 | 100.0 | 200.0 |
| 1873 | 4 | 2 | 0 | 0.8000 | 4 | 0.0 | 0.0 |

## By Property Type

| Property | Test TP | Test FP | Test FN | Test F1 | Value Count | Value MAE | Value MaxErr |
|---|---:|---:|---:|---:|---:|---:|---:|
| elongation | 12 | 2 | 6 | 0.7500 | 12 | 0.3 | 2.7 |
| elongation_compressive | 7 | 5 | 1 | 0.7000 | 7 | 0.0 | 0.0 |
| fracture_strain | 4 | 0 | 0 | 1.0000 | 4 | 0.0 | 0.0 |
| total_elongation | 2 | 6 | 6 | 0.2500 | 2 | 0.0 | 0.0 |
| ultimate_strength_compressive | 7 | 5 | 1 | 0.7000 | 7 | 0.0 | 0.0 |
| ultimate_tensile_strength | 14 | 0 | 6 | 0.8235 | 14 | 73.992857 | 415.5 |
| uniform_elongation | 2 | 0 | 6 | 0.4000 | 2 | 0.0 | 0.0 |
| yield_strength | 26 | 0 | 6 | 0.8966 | 26 | 37.792308 | 270.0 |
| yield_strength_compressive | 12 | 0 | 0 | 1.0000 | 12 | 16.666667 | 200.0 |

## Per Article

### Article `1`
- Composition Detection P/R/F1: `1.0000` / `1.0000` / `1.0000`
- Composition Value MAE: `0.0` (count=4)
- Test Detection P/R/F1: `1.0000` / `1.0000` / `1.0000`
- Test Value MAE: `0.125` (count=8)

### Article `2`
- Composition Detection P/R/F1: `1.0000` / `1.0000` / `1.0000`
- Composition Value MAE: `0.001429` (count=7)
- Test Detection P/R/F1: `0.7222` / `0.9286` / `0.8125`
- Test Value MAE: `7.692308` (count=26)

### Article `3`
- Composition Detection P/R/F1: `1.0000` / `1.0000` / `1.0000`
- Composition Value MAE: `0.0` (count=5)
- Test Detection P/R/F1: `0.6667` / `0.6667` / `0.6667`
- Test Value MAE: `0.0` (count=12)

### Article `4`
- Composition Detection P/R/F1: `0.9167` / `1.0000` / `0.9565`
- Composition Value MAE: `10.757878` (count=11)
- Test Detection P/R/F1: `1.0000` / `1.0000` / `1.0000`
- Test Value MAE: `0.0` (count=16)

### Article `5`
- Composition Detection P/R/F1: `1.0000` / `0.9500` / `0.9744`
- Composition Value MAE: `0.001053` (count=19)
- Test Detection P/R/F1: `1.0000` / `0.2500` / `0.4000`
- Test Value MAE: `0.0` (count=8)

### Article `6`
- Composition Detection P/R/F1: `1.0000` / `1.0000` / `1.0000`
- Composition Value MAE: `0.001111` (count=9)
- Test Detection P/R/F1: `0.8889` / `1.0000` / `0.9412`
- Test Value MAE: `126.31875` (count=16)
