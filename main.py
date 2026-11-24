"""Entrypoint for the grader. Writes a specific text sentence to $MAKEFUN_OUTPUT_DIR/entry.txt."""
# Entry validated: output is 1-320 chars, one sentence, deterministic.

import os
from pathlib import Path

LINE = "The committee drafting the algorithmic transparency act has recessed for three hours because the chairman saved the master file as FINAL_final_v7 (2).docx and nobody knows which draft is the law."

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    dir_path = Path(output_dir)
    dir_path.mkdir(parents=True, exist_ok=True)
    
    file_path = dir_path / "entry.txt"
    content = LINE + "\n"
    
    if not (1 <= len(content) <= 320 and content.strip()):
        raise ValueError("Content validation failed")
        
    file_path.write_text(content, encoding="utf-8")
    
    print(file_path)
    print(len(content))

if __name__ == "__main__":
    main()
