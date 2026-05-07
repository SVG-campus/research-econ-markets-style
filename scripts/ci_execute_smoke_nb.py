"""Execute notebooks/SMOKE_LAYER_A.ipynb headlessly (GitHub Actions)."""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    nb_path = root / "notebooks" / "SMOKE_LAYER_A.ipynb"
    if not nb_path.is_file():
        raise SystemExit(f"missing smoke notebook: {nb_path}")

    import nbformat
    from nbclient import NotebookClient

    nb = nbformat.read(nb_path, as_version=4)
    client = NotebookClient(nb, timeout=120, kernel_name="python3")
    client.execute()
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        for out in cell.get("outputs", []) or []:
            if out.get("output_type") == "error":
                raise SystemExit(f"notebook cell error: {out.get('evalue')}")
    print("OK", nb_path)


if __name__ == "__main__":
    main()
