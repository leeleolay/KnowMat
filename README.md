[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)

# **KnowMat**: Agentic Pipeline for Materials Science Data Extraction

![KnowMat-logo](docs/_static/KnowMat-logo.jpg)

*Figure: Schematic of the KnowMat agentic pipeline for extracting structured materials data from scientific literature.*

---

## Overview

**KnowMat** is an advanced, AI-powered Agentic pipeline that automatically extracts structured, machine-readable materials science data from unstructured scientific literature (`.pdf` / `.txt`). Built on **LangGraph** and powered by **OpenAI-compatible LLM APIs** (including ERNIE/Qianfan), KnowMat orchestrates multiple intelligent agents that collaborate to parse papers, extract compositions, processing conditions, characterization details, and material properties with high accuracy.

### Key Capabilities

- **Research-scale extraction**: Batch process entire folders of PDF/TXT files
- **High accuracy**: Multi-agent architecture with iterative refinement (up to 3 extraction/evaluation cycles)
- **Advanced PDF parsing**: Uses **PaddleOCR-VL** for robust OCR-based PDF parsing
- **Two-stage validation**: Rule-based aggregation + LLM-based hallucination correction
- **Property standardization**: Automatic mapping of property names to standard forms
- **Quality assurance**: Confidence scoring, flagging system for human review (if necessary), and human review guides
- **ML-ready output**: Structured JSON format designed for database ingestion and machine learning

---

## Key Features

### 🤖 **Multi-Agent Architecture**
- **Parser Agent**: PaddleOCR-VL based PDF parsing
  - Converts PDF pages to images and runs OCR page-by-page
  - Stores page images and raw OCR output for debugging
  - Produces clean text for downstream extraction
- **Subfield Detection Agent**: Identifies paper type (experimental/computational/ML) and tailors extraction prompts
- **Extraction Agent**: GPT-5 powered structured data extraction using TrustCall
- **Evaluation Agent**: Iterative quality assessment with confidence scoring (up to 3 cycles)
- **Two-Stage Manager**:
  - **Stage 1 (Aggregation)**: Fast, rule-based merging of extraction runs
  - **Stage 2 (Validation)**: LLM-based hallucination detection and correction
- **Flagging Agent**: Final quality assessment and human review recommendations (if necessary)

### 📊 **Comprehensive Data Extraction**
- Material compositions (elements, stoichiometry, normalized formulas)
- Processing conditions (temperature, pressure, atmosphere, time)
- Characterization methods and results
- Material properties with ML-ready format:
  - Exact values, ranges, inequalities (>, <, ≥, ≤)
  - Numeric extraction with proper handling of qualitative properties
  - Value types: exact, lower_bound, upper_bound, range, qualitative

### 🔬 **Property Standardization**
- Automatic mapping of property names to standard forms using the configured LLM
- Handles symbols, abbreviations, and domain-specific terminology

### 🛡️ **Quality Assurance**
- Confidence scoring for each extraction run
- Hallucination detection using evaluation feedback
- Flagging system for human review
- Detailed rationales and review guides

### ⚡ **Production Features**
- Batch processing of entire PDF folders
- Per-paper output directories with structured organization
- Comprehensive JSON output with extraction metadata
- Human-readable analysis reports
- LangSmith tracing integration for debugging
- Per-agent model configuration for cost/quality optimization

---

## Output Structure

Each processed paper creates a dedicated folder:

```
data/processed/
└── <PaperName>/
    ├── <PaperName>_extraction.json          # Final structured data
    ├── <PaperName>_analysis_report.txt      # Human-readable summary
    ├── <PaperName>_runs.json                # All extraction runs with metadata
    ├── paddleocrvl_parse/                    # Only for PDF inputs
    │   ├── <PaperName>_final_output.md       # Parsed markdown text
    │   ├── <PaperName>_parse_metadata.json   # OCR parser metadata
    │   ├── page_images/                      # Rendered page images
    │   └── ocr_raw/                          # Raw OCR output per page
    └── txt_parse/                            # Only for TXT inputs
        ├── <PaperName>_final_output.md
        └── <PaperName>_parse_metadata.json
```

---

## Installation

### Prerequisites

1. **Python 3.11** with Conda
2. **OpenAI-compatible LLM API key** (e.g. ERNIE/Qianfan)
3. **LangChain API Key** (optional, for LangSmith tracing)

### Setup Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hasan-sayeed/KnowMat2.git
   cd KnowMat2
   ```

2. **Create Conda Environment**:
   ```bash
   conda env create -f environment.yml
   conda activate KnowMat
   ```
   If `paddleocr` installation reports missing backend wheels, install `paddlepaddle` for your platform first and rerun the command.
   If you will process PDF files, pre-download PaddleOCR-VL model files into the project folder:
   ```bash
   python scripts/download_paddleocrvl_models.py --model-dir models/paddleocrvl1_5
   ```

3. **Configure API Keys**:

   Rename the provided example file `.env_example` to `.env` and add your values:
   ```bash
   LLM_API_KEY=<your_llm_api_key_here>
   LLM_BASE_URL=<your_openai_compatible_base_url>
   LLM_MODEL=<your_model_name_or_endpoint>
   PADDLEOCRVL_MODEL_DIR=models/paddleocrvl1_5
   LANGCHAIN_API_KEY=<your_langchain_api_key_here>  # Optional
   LANGCHAIN_TRACING_V2=false  # Optional
   ```

   ERNIE/Qianfan example:
   ```bash
   LLM_API_KEY="bce-v3/xxxx"
   LLM_BASE_URL="https://qianfan.bj.baidubce.com/v2"
   LLM_MODEL="ep_xxxxx"
   ```

   Alternatively, set as environment variables:
   ```bash
   # Windows PowerShell
   $env:LLM_API_KEY="your_key"
   $env:LLM_BASE_URL="https://qianfan.bj.baidubce.com/v2"
   $env:LLM_MODEL="ep_xxxxx"

   # Linux/Mac
   export LLM_API_KEY="your_key"
   export LLM_BASE_URL="https://qianfan.bj.baidubce.com/v2"
   export LLM_MODEL="ep_xxxxx"
   ```

4. **Verify Installation**:
   ```bash
   python -m knowmat --help
   ```

---

## Usage

### Basic Command Line Usage

Process a single folder of files (`.pdf` and/or `.txt`):

```bash
python -m knowmat --input-folder path/to/files --output-dir output/directory
```

Behavior:
- `.pdf` -> uses local PaddleOCR-VL 1.5 model for parsing, then LLM extraction.
- `.txt` -> skips OCR and directly runs LLM extraction using `LLM_API_KEY/LLM_BASE_URL/LLM_MODEL`.

### Advanced Options

```bash
python -m knowmat \
    --input-folder path/to/files \
    --output-dir output/directory \
    --max-runs 1 \
    --workers 4 \
    --extraction-model ${LLM_MODEL} \
    --evaluation-model ${LLM_MODEL} \
    --manager-model ${LLM_MODEL} \
    --subfield-model ${LLM_MODEL} \
    --flagging-model ${LLM_MODEL}
```

### Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--input-folder` | Path to folder containing `.pdf`/`.txt` files | - |
| `--pdf-folder` | Legacy alias of `--input-folder` | - |
| `--output-dir` | Directory for outputs | - |
| `--max-runs` | Maximum extraction/evaluation cycles | `1` |
| `--workers` | Number of files processed concurrently | `1` |
| `--full-pipeline` | Enable full multi-stage pipeline | `False` |
| `--enable-property-standardization` | Enable optional property matching post-process | `False` |
| `--subfield-model` | Model for subfield detection | `LLM_MODEL` |
| `--extraction-model` | Model for data extraction | `LLM_MODEL` |
| `--evaluation-model` | Model for quality evaluation | `LLM_MODEL` |
| `--manager-model` | Model for validation (Stage 2) | `LLM_MODEL` |
| `--flagging-model` | Model for final quality assessment | `LLM_MODEL` |

### Python API

```python
from knowmat.orchestrator import run
import os

result = run(
    pdf_path="path/to/paper.pdf",  # Also supports .txt path
    output_dir="data/processed",
    max_runs=3,
    # Per-agent overrides:
    subfield_model=os.getenv("LLM_MODEL"),
    extraction_model=os.getenv("LLM_MODEL"),
    evaluation_model=os.getenv("LLM_MODEL"),
    manager_model=os.getenv("LLM_MODEL"),
    flagging_model=os.getenv("LLM_MODEL"),
)

print(f"Extracted {len(result['final_data']['compositions'])} compositions")
print(f"Confidence: {result.get('confidence_score', 0):.2f}")
print(f"Flagged: {result['flag']}")
```

---

### Output Examples

**JSON Output Structure**

```json
{
  "compositions": [
    {
      "composition": "Zr64.13Cu15.75Ni10.12Al10",
      "composition_normalized": "Zr64Cu16Ni10Al10",
      "processing_conditions": {
        "method": "melt spinning",
        "temperature": "1400 K",
        "cooling_rate": "10^6 K/s",
        "atmosphere": "argon"
      },
      "characterization": {
        "XRD": "amorphous structure confirmed",
        "DSC": "glass transition at 625 K; crystallization at 705 K"
      },
      "properties_of_composition": [
        {
          "property_name": "glass transition temperature",
          "property_symbol": "Tg",
          "value": "625",
          "value_numeric": 625.0,
          "value_type": "exact",
          "units": "K"
        },
        {
          "property_name": "fracture strength",
          "property_symbol": "σ_max",
          "value": ">1800",
          "value_numeric": 1800.0,
          "value_type": "lower_bound",
          "units": "MPa"
        }
      ]
    }
  ]
}
```

---

## Project Organization

```
├── AUTHORS.md              <- List of developers and maintainers
├── CHANGELOG.md            <- Changelog to keep track of new features and fixes
├── CONTRIBUTING.md         <- Guidelines for contributing to this project
├── LICENSE.txt             <- MIT License
├── README.md               <- This file
├── environment.yml         <- Conda environment specification
├── pyproject.toml          <- Build configuration
├── setup.cfg               <- Package metadata and dependencies
├── setup.py                <- Setup script (deprecated, use pip install -e .)
│
├── configs/                <- Configuration files
│   └── properties.json     <- Property database for standardization
│
├── data/
│   ├── raw/                <- Original, immutable source files (.pdf/.txt)
│   └── processed/          <- Extracted structured data
│       └── <PaperName>/    <- Per-paper output folders
│
├── src/
│   └── knowmat/            <- Main package
│       ├── __init__.py
│       ├── __main__.py     <- CLI entry point
│       ├── orchestrator.py <- Pipeline orchestration (LangGraph)
│       ├── app_config.py   <- Settings and configuration
│       ├── config.py       <- Environment setup
│       ├── states.py       <- LangGraph state definitions
│       ├── extractors.py   <- Pydantic schemas for TrustCall
│       ├── prompt_generator.py <- Dynamic prompt generation
│       ├── post_processing.py  <- Property standardization
│       └── nodes/          <- Agent implementations
│           ├── paddleocrvl_parse_pdf.py  <- Parser agent
│           ├── subfield_detection.py <- Subfield agent
│           ├── extraction.py         <- Extraction agent
│           ├── evaluation.py         <- Evaluation agent
│           ├── aggregator.py         <- Manager Stage 1
│           ├── validator.py          <- Manager Stage 2
│           └── flagging.py           <- Flagging agent
│
├── tests/                  <- Unit tests (pytest)
├── notebooks/              <- Jupyter notebooks for analysis
└── docs/                   <- Sphinx documentation
```

---

## Advanced Features

### Two-Stage Manager Architecture

KnowMat's unique two-stage manager architecture separates data merging from validation:

**Stage 1 - Aggregation (Rule-Based)**:
  - Fast, deterministic merging of extraction runs
  - No LLM calls (zero cost, zero latency)
  - Selects highest-confidence run as base
  - Merges additional compositions from other runs

**Stage 2 - Validation (LLM-Based)**:
- Focused hallucination detection using evaluation feedback
- Correction of hallucinated properties
- ML-ready format validation
- Safety checks for placeholder responses
- Retry mechanism with stronger prompts
- Human review guide generation

### Property Standardization

The PostProcessor uses the configured LLM to intelligently map extracted property names to standard forms.

**Example Mappings**:
- "Dimensionless figure of merit ZT" → "thermoelectric figure of merit"
- "glass transition temp" → "glass transition temperature"
- "ultimate tensile strength" → "tensile strength"
- "Young's modulus" → "elastic modulus"

### Batch Processing

Process hundreds of papers efficiently:

```bash
# Process entire folder
python -m knowmat --input-folder data/raw/papers --output-dir data/processed

# Console shows progress for each paper
Processing file 1/150: paper001.pdf
Processing file 2/150: notes002.txt
...

# Final summary
Total files: 150
Successful: 147
Failed: 3
Flagged for review: 23
Total compositions: 2,341
```

### LangSmith Tracing

KnowMat integrates with LangSmith for comprehensive debugging and tracing of all LLM decisions.

With tracing enabled, you can:
- View every LLM call and response in the LangSmith dashboard
- Debug extraction decisions and prompt effectiveness
- Analyze confidence scoring rationale
- Trace multi-agent interactions through the entire pipeline
- Monitor token usage and costs per paper

Access your traces at: https://smith.langchain.com/

---

## Model Selection and Cost Optimization

KnowMat supports per-agent model configuration, allowing you to balance cost and accuracy.
When using ERNIE/Qianfan, set `LLM_MODEL` and optionally override per-agent models.

### Recommended Configuration (Production)

```bash
--subfield-model ${LLM_MODEL}
--extraction-model ${LLM_MODEL}
--evaluation-model ${LLM_MODEL}
--manager-model ${LLM_MODEL}
--flagging-model ${LLM_MODEL}
```

---

## Troubleshooting

### Common Issues

**1. API Key Errors**
```
Error: LLM_API_KEY not set
```
**Solution**: Configure `LLM_API_KEY`, `LLM_BASE_URL`, and `LLM_MODEL` according to the [Configure API Keys](#configure-api-keys) section.
```bash
export LLM_API_KEY="your_key"
export LLM_BASE_URL="https://qianfan.bj.baidubce.com/v2"
export LLM_MODEL="ep_xxxxx"
```

**2. PaddleOCR-VL Parsing Failures**
```
Error: Failed to parse PDF with PaddleOCR-VL
```
**Solution**: Ensure PDF is not corrupted or password-protected. Try re-downloading the PDF.

**3. Property Standardization Failures**
```
Warning: Property standardization failed
```
**Solution**: Ensure `src/knowmat/properties.json` exists and is valid JSON.

---

## Roadmap

- [ ] **Web Interface**: Reimplement Flask UI for non-technical users
- [ ] **Database Integration**: Direct export to PostgreSQL/MongoDB
- [ ] **Scientific Figure Extraction**: Capture quantitative data from charts, graphs, and plots in scientific figures
- [ ] **Domain Expansion**: Support for chemistry, biology, and physics papers

---

## Citation

If you use KnowMat in your research, please cite:

```bibtex
@software{knowmat2024,
  title = {KnowMat: Agentic Pipeline for Materials Science Data Extraction},
  author = {Sayeed, Hasan},
  year = {2024},
  url = {https://github.com/hasan-sayeed/KnowMat2}
}
```

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**How to contribute**:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see [LICENSE.txt](LICENSE.txt) for details.

---

## Acknowledgments

- Built with [PyScaffold](https://pyscaffold.org/)
- Powered by [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain)
- PDF parsing by [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- Inspired by the MI-Agent architecture

---

## Support

For questions, bug reports, or feature requests:
- **GitHub Issues**: https://github.com/hasan-sayeed/KnowMat2/issues
- **Email**: hasan.sayeed@utah.edu



<!-- pyscaffold-notes -->

## Note

This project has been set up using [PyScaffold] 4.6 and the [dsproject extension] 0.7.2.

[conda]: https://docs.conda.io/
[pre-commit]: https://pre-commit.com/
[Jupyter]: https://jupyter.org/
[nbstripout]: https://github.com/kynan/nbstripout
[Google style]: http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[PyScaffold]: https://pyscaffold.org/
[dsproject extension]: https://github.com/pyscaffold/pyscaffoldext-dsproject
