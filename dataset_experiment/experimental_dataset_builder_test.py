from tensorflow_datasets import testing
from dataset_experiment import experimental_dataset_builder


class ExperimentalDatasetTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = experimental_dataset_builder.Builder
  SPLITS = {  # Expected number of examples on each split.
      "train": 5,
      "test": 5,
  }

  DL_EXTRACT_RESULT = {
      "images": ".",
      "annotations": ".",
  }


if __name__ == "__main__":
  testing.test_main()
