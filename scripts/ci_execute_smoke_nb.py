"""Execute notebooks listed in runs/ci_notebooks.yaml (GitHub Actions).

Falls back to `notebooks/SMOKE_LAYER_A.ipynb` if the config file is absent.

Rows may set `enabled: false` to keep charter notebook paths in-repo without
executing them in CI yet.
"""

from __future__ import annotations

from pathlib import Path


def _load_jobs(root: Path) -> list[tuple[Path, int]]:
    cfg = root / "runs" / "ci_notebooks.yaml"
    if not cfg.is_file():
        return [(root / "notebooks" / "SMOKE_LAYER_A.ipynb", 120)]

    import yaml

    data = yaml.safe_load(cfg.read_text(encoding="utf-8")) or {}
    jobs: list[tuple[Path, int]] = []
    for row in data.get("notebooks", []):
        if row.get("enabled", True) is False:
            continue
        rel = row.get("path")
        if not rel:
            continue
        jobs.append((root / rel, int(row.get("timeout_seconds", 120))))
    if not jobs:
        return [(root / "notebooks" / "SMOKE_LAYER_A.ipynb", 120)]
    return jobs


def _execute_one(nb_path: Path, timeout: int) -> None:
    import nbformat
    from nbclient import NotebookClient

    nb = nbformat.read(nb_path, as_version=4)
    client = NotebookClient(nb, timeout=timeout, kernel_name="python3")
    client.execute()
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        for out in cell.get("outputs", []) or []:
            if out.get("output_type") == "error":
                raise SystemExit(f"{nb_path}: {out.get('evalue')}")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    for nb_path, timeout in _load_jobs(root):
        if not nb_path.is_file():
            raise SystemExit(f"missing notebook: {nb_path}")
        _execute_one(nb_path, timeout)
        print("OK", nb_path)


if __name__ == "__main__":
    main()
