import subprocess
from pathlib import Path


def test_cli_module(tmp_path):
    outdir = str(tmp_path / "dir1/dir2")
    args = f"python3 -m simplelayout --board_grid 100 --unit_grid 10 --unit_n 3 --positions 1 15 33 --outdir {outdir} --file_name example"  # noqa
    ret = subprocess.run(
        args,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        timeout=2,
    )
    assert ret.returncode == 0, ret.stderr
    path_mat = Path(outdir) / "example.mat"
    path_jpg = path_mat.with_suffix(".jpg")
    assert path_mat.exists(), "mat 文件不存在"
    assert path_jpg.exists(), "jpg 文件不存在"
