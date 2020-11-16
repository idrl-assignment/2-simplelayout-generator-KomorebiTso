from simplelayout.generator.utils import save_matrix, save_fig, make_dir
import numpy as np
import scipy.io as sio
from pathlib import Path


def test_mat(tmp_path):
    file_name = "tmp"
    path = tmp_path / file_name
    path_suffix = tmp_path / f"{file_name}.mat"
    matrix = np.random.randint(0, 2, size=(3, 3))
    save_matrix(matrix, file_name=str(path))
    assert path_suffix.exists(), "mat 文件不存在"

    matrix_loaded = sio.loadmat(path_suffix)["matrix"]
    assert np.array_equal(matrix_loaded, matrix), "mat 文件数据异常"


def test_jpg(tmp_path):
    file_name = "tmp"
    path = tmp_path / file_name
    save_fig(np.zeros((3, 3)), file_name=str(path))
    assert (tmp_path / f"{file_name}.jpg").exists(), "jpg 文件不存在"


def test_mkdir(tmp_path):
    outdir = "dir1/dir2"
    path = Path(outdir)
    make_dir(outdir)
    assert path.exists(), "dir1/dir2 不存在"

    make_dir(outdir)
    assert path.exists(), "当 dir1/dir2 已存在时，发生错误"
