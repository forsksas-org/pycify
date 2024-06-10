"""CLI interface for pycify."""
from __future__ import annotations

import argparse

from pycify import replace_py_with_pyc


class PycifyArgs:
    directory: str
    out_dir: str
    optimize: str


def cli(argv: list[str] | None = None) -> None:
    """CLI to run pycify."""
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="Folder to convert .py files in")
    parser.add_argument(
        "--out-dir",
        help=(
            "Folder to output .pyc files to. "
            "Defaults to replacing the existing `.py` files."
        ),
    )
    parser.add_argument(
        "--optimize",
        help=(
            "Specifies the optimization level for the compiler."
            "Accepts a sequence of optimization levels which lead to multiple "
            "compilations of one .py file in one call."
            "For example: 1,2 or 2,1,1,2 or 2"
        )
    )
    args = parser.parse_args(argv, namespace=PycifyArgs)
    replace_py_with_pyc(args.directory, out_folder=args.out_dir,
                        optimize=args.optimize)
