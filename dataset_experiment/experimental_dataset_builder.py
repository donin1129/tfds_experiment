import os
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_BASE_URL = "https:"  # TODO: Add Base URL


class Builder(tfds.core.GeneratorBasedBuilder):

  VERSION = tfds.core.Version("0.0.1")
  LOCAL_PATH = None

  def set_local_path(self, path):
    self.LOCAL_PATH = path

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "domain_a_image": tfds.features.Image(),
            "domain_a_image_filename": tfds.features.Text(),
            "domain_b_image": tfds.features.Image(),
            "domain_b_image_filename": tfds.features.Text(),
        }),
    )

  def _split_generators(self, dl_manager):

    if self.LOCAL_PATH is None:

        dl_paths = dl_manager.download_and_extract({
            "images": _BASE_URL + "/images.tar.gz",
            "annotations": _BASE_URL + "/annotations.tar.gz",
        })

        images_path_dir = os.path.join(dl_paths["images"], "images")
        annotations_path_dir = os.path.join(dl_paths["annotations"], "annotations")

    else:

        images_path_dir = os.path.join(self.LOCAL_PATH, "images")
        annotations_path_dir = os.path.join(self.LOCAL_PATH, "annotations")

    # Setup train and test splits
    train_split = tfds.core.SplitGenerator(
        name="train",
        gen_kwargs={
            "images_dir_path": images_path_dir,
            "annotations_dir_path": annotations_path_dir,
            "images_list_file": os.path.join(
                annotations_path_dir, "trainval.txt"
            ),
        },
    )
    test_split = tfds.core.SplitGenerator(
        name="test",
        gen_kwargs={
            "images_dir_path": images_path_dir,
            "annotations_dir_path": annotations_path_dir,
            "images_list_file": os.path.join(annotations_path_dir, "test.txt"),
        },
    )

    return [train_split, test_split]

  def _generate_examples(
      self, images_dir_path, annotations_dir_path, images_list_file
  ):
    with tf.io.gfile.GFile(images_list_file, "r") as images_list:
      for line in images_list:
        image_name = line.strip()

        trimaps_dir_path = os.path.join(annotations_dir_path, "trimaps")

        trimap_name = image_name + ".png"
        image_name += ".png"

        record = {
            "domain_a_image": os.path.join(images_dir_path, image_name),
            "domain_a_image_filename": image_name,
            "domain_b_image": os.path.join(trimaps_dir_path, trimap_name),
            "domain_b_image_filename": trimap_name,
        }
        yield image_name, record
