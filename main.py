"""Write the 20 November 2026 front page to the output directory.

The picture shipped with this repository, entry.png, is a newspaper front
page drawn from the morning's reporting on Friday 20 November 2026. It
leads with Anthropic's first day on the Nasdaq, then the peace declaration
from the first Trump-Xi-Putin summit, the World Court's genocide verdict
on Myanmar, the widening war in the Gulf, the overnight strikes on Kyiv,
Bitcoin falling below $62,000, Jakarta's Asset Forfeiture Bill, and the
COP31 draft dropping fossil fuels, with shorter briefs along the foot.

Running this file does one job: it places an exact copy of that picture
at $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png when the variable
is unset). It opens no sockets, reads no clock and rolls no dice, so the
file it writes is the same on every run. Before it reports success it
re-reads what it wrote and confirms the signature, the size and the full
contents match the picture stored here.
"""

import hashlib
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STORED = HERE / "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
ONE_MIB = 1_048_576


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_picture() -> bytes:
    """Read the stored front page and confirm it is a whole PNG."""
    data = STORED.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("stored entry.png does not start with the PNG signature")
    if len(data) > ONE_MIB:
        raise ValueError("stored entry.png is larger than the 1 MiB limit")
    return data


def place_picture(data: bytes) -> Path:
    """Write the picture to the output folder and prove the copy is exact."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    written = target.read_bytes()
    if not written.startswith(PNG_SIGNATURE):
        raise ValueError("output does not start with the PNG signature")
    if digest(written) != digest(data):
        raise ValueError("output bytes differ from the stored picture")
    if len(written) > ONE_MIB:
        raise ValueError("output is larger than the 1 MiB limit")
    return target


def main() -> int:
    try:
        data = load_picture()
        target = place_picture(data)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr, flush=True)
        return 1
    print(f"wrote {target} ({target.stat().st_size} bytes)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
