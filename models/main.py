from pathlib import Path
from models.nns import Model
import models.utils.image_processor as imp


if __name__ == '__main__':
    # Define paths
    img_path = Path("temp")
    # Training and validation paths
    original_img_path = img_path.joinpath("original")
    processed_img_path = img_path.joinpath("processed")
    # Original paths
    original_training = original_img_path.joinpath("processed")
    original_validation = original_img_path.joinpath("validation")
    # Processed paths
    processed_training = processed_img_path.joinpath("processed")
    processed_validation = processed_img_path.joinpath("validation")
    # Model output path
    output_path = Path("models")
    # Resize images
    IMG_HEIGHT = 224
    IMG_WIDTH = 224
    imp.resize_images_in(original_training, processed_training, IMG_HEIGHT, IMG_WIDTH)
    imp.resize_images_in(original_validation, processed_validation, IMG_HEIGHT, IMG_WIDTH)
    # Get new model
    model = Model(processed_img_path, (IMG_HEIGHT, IMG_WIDTH))
    model.model.save(output_path, include_optimizer=True)
