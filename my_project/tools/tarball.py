import argparse
import tarfile

from pathlib import Path

FIXED_TIME = 0


def reset(tarinfo: tarfile.TarInfo):
    """Resets file info to deterministic values."""
    tarinfo.uid = 0
    tarinfo.gid = 0
    tarinfo.uname = "root"
    tarinfo.gname = "root"
    tarinfo.mtime = FIXED_TIME
    return tarinfo


def main(
    bin: Path,
    output: Path,
) -> None:
    """Creates a package from input binary."""

    with tarfile.open(output.as_posix(), "w:gz") as f:
        f.add(bin.as_posix(), arcname=bin.name, filter=reset)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Pack", description="Creates a hypothetical package"
    )
    parser.add_argument("--bin", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    main(args.bin, args.output)
