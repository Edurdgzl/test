import cv2
from pathlib import Path
import models.utils.file_handler as fh


def resize_image(image_path: str | Path, output_path: str | Path, height: int, width: int) -> None:
    original = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(original, (width, height), interpolation=cv2.INTER_AREA)
    cv2.imwrite(output_path, resized)


def resize_images_in(source_dir: str | Path, output_dir: str | Path, height: int, width: int) -> None:
    source_path = fh.to_path(source_dir)
    output_parent = fh.to_path(output_dir)
    fh.copy_subdirs_from(source_dir, output_dir)
    for child in source_path.rglob('*'):
        if child.is_file():
            output_path = output_parent.joinpath(child.parent.name, child.name)
            resize_image(child, output_path, height, width)
