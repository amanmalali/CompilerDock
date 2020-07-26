import os
import tempfile

import pytest

from src.config import BASE_PATH, FileNames
from src.utils import files


@pytest.fixture(scope="class")
def temp_dir():
    dir_path = f"{BASE_PATH}/temp"
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        pass
    with tempfile.TemporaryDirectory(dir=dir_path) as dest:
        yield dest


class TestFiles:
    def test_init_dir(self, temp_dir):
        files.init_dir(dest=temp_dir, filenames=[FileNames.output.value])
        file_names = os.listdir(path=temp_dir)
        assert FileNames.output.value in file_names

    def test_read_ouput(self, temp_dir):
        output = files.read_ouput(temp_dir, FileNames.output.value)
        assert "" == output

    @pytest.mark.parametrize(
        "file_name, data", [("error_file1", ""), ("error_file2", "some data")]
    )
    def test_create_files(self, temp_dir, file_name, data):
        files.create_files(data, file_name, temp_dir)
        file_names = os.listdir(path=temp_dir)
        assert file_name in file_names

    @pytest.mark.parametrize(
        "file_name, expected_error",
        [("error_file1", ("", False)), ("error_file2", ("some data", True))],
    )
    def test_error_check(self, temp_dir, file_name, expected_error):
        error_val = files.error_check(temp_dir, file_name)
        assert error_val == expected_error
