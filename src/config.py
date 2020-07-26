import enum
import os


class FileNames(enum.Enum):
    error = "errors"
    completed = "completed"
    input = "input"
    output = "output"


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
comp = ["c", "c++", "rust"]
exe = {"c": " ./a.out", "c++": " ./a.out", "rust": " ./file"}
inter = {
    "python3": "python3",
    "c": "gcc",
    "c++": "g++",
    "java": "java",
    "go": '"go run"',
    "R": "Rscript",
    "PHP": "php",
    "ruby": "ruby",
    "rust": "rustc",
}
filenames = {
    "python3": "file.py",
    "c": "file.c",
    "c++": "file.cpp",
    "java": "file.java",
    "go": "file.go",
    "R": "file.r",
    "PHP": "file.php",
    "ruby": "file.rb",
    "rust": "file.rs",
}
