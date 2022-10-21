from __future__ import annotations
from pathlib import Path


def is_valid_path(path) -> bool:
    if isinstance(path, str) or isinstance(path, Path):
        return True
    else:
        return False


def to_path(path: str | Path) -> Path:
    return_obj = path
    if is_valid_path(path):
        if isinstance(path, str):
            return_obj = Path(path)
    else:
        raise TypeError(f"{type(path)} is not supported by file_handler.")
    return return_obj


def to_str(path: str | Path) -> str:
    if isinstance(path, Path):
        return str(path)
    else:
        return path


def get_subdir_names_from(path: str | Path) -> list:
    curr_path = to_path(path)
    subdirs = []
    for child in curr_path.rglob('*'):
        if child.is_dir():
            subdirs.append(child.name)
    return subdirs


def create_dirs(*dirs: str | Path):
    for path in dirs:
        path = to_path(path)
        if not path.exists():
            path.mkdir()


def copy_subdirs_from(source: str | Path, other: str | Path) -> None:
    new_path_parent = to_path(other).absolute()
    create_dirs(new_path_parent)
    for name in get_subdir_names_from(source):
        new_path = new_path_parent.joinpath(name)
        if not new_path.exists():
            new_path.mkdir()


def empty_dir(source: str | Path) -> None:
    source = to_path(source)
    if source.is_dir():
        for child in source.rglob('*'):
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                empty_dir(child)


def clean_creation(path: str | Path) -> Path | None:
    path = to_path(path)
    if not path.exists():
        path.mkdir()
    else:
        empty_dir(path)
    return path
