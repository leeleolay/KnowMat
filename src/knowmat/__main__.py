"""
Entry point for running the KnowMat 2.0 pipeline via the command line.

Usage
-----
::

    python -m knowmat --input-folder path/to/files [--output-dir out] [--max-runs 1]

This will parse all supported files (PDF/TXT) in the given folder, run the
agentic extraction workflow and write the results to the specified output
directory. Each file is processed
sequentially. The final JSON, rationale and intermediate run records are saved
separately for each paper.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from knowmat.orchestrator import run


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run the KnowMat 2.0 extraction pipeline for PDF/TXT inputs.")
    parser.add_argument("--input-folder", default=None, help="Path to the folder containing PDF/TXT files to process.")
    parser.add_argument("--pdf-folder", default=None, help="Legacy alias of --input-folder.")
    parser.add_argument("--output-dir", default=None, help="Directory to write outputs to (default: ./knowmat_output).")
    parser.add_argument("--max-runs", type=int, default=1, help="Maximum extraction/evaluation cycles.")
    parser.add_argument("--workers", type=int, default=1, help="Number of files to process concurrently.")
    parser.add_argument("--full-pipeline", action="store_true", help="Enable full multi-stage pipeline.")
    parser.add_argument(
        "--enable-property-standardization",
        action="store_true",
        help="Enable optional property standardization (slower, more LLM calls).",
    )
    
    # Per-agent model overrides
    parser.add_argument("--subfield-model", default=None, help="Model for subfield detection agent.")
    parser.add_argument("--extraction-model", default=None, help="Model for extraction agent.")
    parser.add_argument("--evaluation-model", default=None, help="Model for evaluation agent.")
    parser.add_argument("--manager-model", default=None, help="Model for validation agent (Stage 2: hallucination correction).")
    parser.add_argument("--flagging-model", default=None, help="Model for flagging/quality assessment agent.")
    
    args = parser.parse_args(argv)
    
    input_folder_arg = args.input_folder or args.pdf_folder
    if not input_folder_arg:
        print("Error: Please provide --input-folder (or legacy --pdf-folder).")
        return

    input_folder = Path(input_folder_arg)
    if not input_folder.exists():
        print(f"Error: Input folder not found: {input_folder}")
        return
    
    if not input_folder.is_dir():
        print(f"Error: Path is not a directory: {input_folder}")
        return
    
    input_files = sorted(
        [
            p for p in input_folder.iterdir()
            if p.is_file() and p.suffix.lower() in {".pdf", ".txt"}
        ],
        key=lambda x: x.name.lower(),
    )
    
    if not input_files:
        print(f"Error: No supported files (.pdf/.txt) found in: {input_folder}")
        return
    
    print(f"\nFound {len(input_files)} files (.pdf/.txt) to process")
    print("=" * 60)
    
    def _process_one(file_path: Path) -> dict:
        try:
            result = run(
                pdf_path=str(file_path),
                output_dir=args.output_dir,
                model_name=None,  # Use defaults from settings
                max_runs=args.max_runs,
                subfield_model=args.subfield_model,
                extraction_model=args.extraction_model,
                evaluation_model=args.evaluation_model,
                manager_model=args.manager_model,
                flagging_model=args.flagging_model,
                full_pipeline=args.full_pipeline,
                enable_property_standardization=args.enable_property_standardization,
            )

            materials = result.get("final_data", {}).get("Materials", [])
            compositions_count = len(materials)
            return {
                "file": file_path.name,
                "success": True,
                "flag": result.get("flag"),
                "compositions": compositions_count,
                "output_dir": result.get("output_dir"),
            }
        except Exception as e:
            return {"file": file_path.name, "success": False, "error": str(e)}

    results_summary = []
    workers = max(1, args.workers)
    if workers == 1:
        for i, file_path in enumerate(input_files, 1):
            print(f"\n{'='*60}")
            print(f"Processing file {i}/{len(input_files)}: {file_path.name}")
            print(f"{'='*60}\n")
            summary = _process_one(file_path)
            results_summary.append(summary)
            if summary["success"]:
                flag_str = "[FLAGGED]" if summary.get("flag") else "[OK]"
                print(f"\nFinished extraction: {file_path.name}")
                print(f"   Status: {flag_str}")
                print(f"   Output: {summary.get('output_dir')}")
                print(f"   Materials: {summary.get('compositions', 0)}")
            else:
                print(f"\nError processing {file_path.name}: {summary.get('error')}")
    else:
        print(f"Running with {workers} workers...")
        with ThreadPoolExecutor(max_workers=workers) as pool:
            fut_map = {pool.submit(_process_one, p): p for p in input_files}
            for fut in as_completed(fut_map):
                summary = fut.result()
                results_summary.append(summary)
                if summary["success"]:
                    flag_str = "[FLAGGED]" if summary.get("flag") else "[OK]"
                    print(f"{flag_str} {summary['file']}: {summary.get('compositions', 0)} materials")
                else:
                    print(f"[ERROR] {summary['file']}: {summary.get('error')}")
    
    # Print final summary
    print(f"\n{'='*60}")
    print("PROCESSING SUMMARY")
    print(f"{'='*60}\n")
    
    successful = sum(1 for r in results_summary if r['success'])
    failed = len(results_summary) - successful
    
    print(f"Total files: {len(results_summary)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    
    if successful > 0:
        flagged = sum(1 for r in results_summary if r['success'] and r.get('flag'))
        print(f"Flagged for review: {flagged}")
        total_compositions = sum(r.get('compositions', 0) for r in results_summary if r['success'])
        print(f"Total materials: {total_compositions}")
    
    print(f"\n{'='*60}\n")
    
    # Print individual results
    for r in results_summary:
        if r['success']:
            flag_icon = "[FLAGGED]" if r['flag'] else "[OK]"
            print(f"{flag_icon} {r['file']}: {r['compositions']} materials")
        else:
            print(f"[ERROR] {r['file']}: {r.get('error', 'Unknown error')}")


if __name__ == "__main__":  # pragma: no cover
    main()
