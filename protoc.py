# -*- coding: utf-8 -*-
import subprocess
from subprocess import CalledProcessError

import typer

app = typer.Typer()


@app.command()
def version() -> None:
    result = subprocess.run(
        ["poetry", "run", "python", "-m", "grpc.tools.protoc", "--version"], capture_output=True, encoding="utf-8"
    )

    try:
        result.check_returncode()
        print(result.stdout)
    except CalledProcessError:
        print(result.stderr)


@app.command()
def generate() -> None:
    result = subprocess.run(
        [
            "poetry",
            "run",
            "python",
            "-m",
            "grpc.tools.protoc",
            "--proto_path",
            "./protos",
            "--python_out",
            "./protos",
            "--mypy_out",
            "./protos",
            "--grpc_python_out",
            "./protos",
            "./protos/*.proto", 
        ],
        capture_output=True,
        encoding="utf-8",
    )

    try:
        result.check_returncode()
        print("Python module generated")
    except CalledProcessError:
        print(result.stderr)

if __name__ == "__main__":
    app()
