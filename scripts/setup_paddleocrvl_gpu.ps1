param(
    [string]$ModelDir = $null
)

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
if (-not $ModelDir) {
    $ModelDir = Join-Path $repoRoot "models\paddleocrvl1_5"
}
$ModelDir = [System.IO.Path]::GetFullPath($ModelDir)
New-Item -ItemType Directory -Force -Path $ModelDir | Out-Null

# Configure runtime defaults for PaddleOCR-VL
$env:KNOWMAT_OCR_DEVICE = "gpu:0"
$env:PADDLEOCR_HOME = $ModelDir
$env:PADDLE_PDX_CACHE_HOME = $ModelDir
$env:PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK = "True"

$python = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
    $python = "python"
}

Write-Host "Using Python: $python"
Write-Host "Model cache dir: $ModelDir"

& $python -m pip install --upgrade pip

# PaddleOCR-VL (Blackwell / RTX 50-series) GPU setup
& $python -m pip install paddlepaddle-gpu==3.2.1 -i https://www.paddlepaddle.org.cn/packages/stable/cu129/
& $python -m pip install -U "paddleocr[doc-parser]"
& $python -m pip install -U "beautifulsoup4==4.12.3"

# One-click model download into project-local cache
& $python scripts\download_paddleocrvl_models.py --model-dir $ModelDir
