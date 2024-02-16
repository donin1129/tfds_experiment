from dataset_experiment import experimental_dataset_builder
import matplotlib.pyplot as plt


def build_dataset_b_download(name):
    builder = experimental_dataset_builder.Builder()
    builder.download_and_prepare()
    train_ds = builder.as_dataset(split='train')
    train_ds_reduced = builder.as_dataset(split='train[:75%]')
    test_ds = builder.as_dataset(split='test')

    train_sample = next(iter(train_ds))
    train_sample_reduced = next(iter(train_ds_reduced))
    test_sample = next(iter(test_ds))

    # show train samples here
    img_a_msk = train_sample['domain_a_image']
    img_a_filename = train_sample['domain_a_image_filename']
    img_b_msk = train_sample['domain_b_image']
    img_b_filename = train_sample['domain_b_image_filename']

    plt.imshow(img_a_msk)
    plt.imshow(img_b_msk)
    print(img_a_filename)
    print(img_b_filename)

    # show train samples reduced here
    img_a_msk = train_sample_reduced['domain_a_image']
    img_a_filename = train_sample_reduced['domain_a_image_filename']
    img_b_msk = train_sample_reduced['domain_b_image']
    img_b_filename = train_sample_reduced['domain_b_image_filename']

    plt.imshow(img_a_msk)
    plt.imshow(img_b_msk)
    print(img_a_filename)
    print(img_b_filename)

    # show test samples reduced here
    img_a_msk = test_sample['domain_a_image']
    img_a_filename = test_sample['domain_a_image_filename']
    img_b_msk = test_sample['domain_b_image']
    img_b_filename = test_sample['domain_b_image_filename']

    plt.imshow(img_a_msk)
    plt.imshow(img_b_msk)
    print(img_a_filename)
    print(img_b_filename)

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def build_dataset_f_local_path(name):
    builder = experimental_dataset_builder.Builder()
    builder.set_local_path("./dummy_data")  # TODO: Add local file path
    builder.download_and_prepare()
    train_ds = builder.as_dataset(split='train')
    train_ds_reduced = builder.as_dataset(split='train[:75%]')
    test_ds = builder.as_dataset(split='test')

    train_sample = next(iter(train_ds))
    train_sample_reduced = next(iter(train_ds_reduced))
    test_sample = next(iter(test_ds))

    # show train samples here
    img_a_msk = train_sample['domain_a_image']
    img_a_filename = train_sample['domain_a_image_filename']
    img_b_msk = train_sample['domain_b_image']
    img_b_filename = train_sample['domain_b_image_filename']

    plt.imshow(img_a_msk)
    plt.imshow(img_b_msk)
    print(img_a_filename)
    print(img_b_filename)

    # show train samples reduced here
    img_a_msk = train_sample_reduced['domain_a_image']
    img_a_filename = train_sample_reduced['domain_a_image_filename']
    img_b_msk = train_sample_reduced['domain_b_image']
    img_b_filename = train_sample_reduced['domain_b_image_filename']

    plt.imshow(img_a_msk)
    plt.imshow(img_b_msk)
    print(img_a_filename)
    print(img_b_filename)

    # show test samples reduced here
    img_a_msk = test_sample['domain_a_image']
    img_a_filename = test_sample['domain_a_image_filename']
    img_b_msk = test_sample['domain_b_image']
    img_b_filename = test_sample['domain_b_image_filename']

    plt.imshow(img_a_msk)
    plt.imshow(img_b_msk)
    print(img_a_filename)
    print(img_b_filename)

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    build_dataset_f_local_path('PyCharm')
    build_dataset_b_download('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
