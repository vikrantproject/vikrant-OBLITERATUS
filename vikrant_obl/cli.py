"""CLI entry point for vikrant-OBLITERATUS."""

import argparse
from rich.console import Console

console = Console()

def main():
    parser = argparse.ArgumentParser(
        prog="vobl",
        description="vikrant-OBLITERATUS: Advanced Abliteration Framework"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # obliterate
    obl = subparsers.add_parser("obliterate", help="Remove refusal directions")
    obl.add_argument("model", help="Model name")
    obl.add_argument("--method", default="svd_normpres")
    obl.add_argument("--auto-finetune", action="store_true")
    
    # scan
    scan = subparsers.add_parser("scan", help="Security scan")
    scan.add_argument("model", help="Model name")
    scan.add_argument("--deep", action="store_true")
    
    # ui
    subparsers.add_parser("ui", help="Launch Gradio UI")
    
    args = parser.parse_args()
    console.print(f"[green]vobl {args.command}[/green]")
    console.print("vikrant-OBLITERATUS v2.0.0 - Framework initialized")
    
if __name__ == "__main__":
    main()
