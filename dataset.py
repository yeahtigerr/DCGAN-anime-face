import torch
import torch.utils.data
import numpy as np
import scipy.misc
import os


class Dataset(torch.utils.data.Dataset):

    def __init__(self, dir, dataset, size_per_dataset):
        self.directory = dir
        self.dataset = dataset
        self.size_per_dataset = size_per_dataset
        self.data_files = []
        data_path = os.path.join(directory, dataset)
        for i in range(size_per_dataset):
            self.data_files.append(os.path.join(data_path, "{}.jpg".format(i)))

    def __getitem__(self, item):
        path = self.data_files[item]
        img = scipy.misc.imread(path)
        img = img.transpose(2, 0, 1) - 127.5 / 127.5
        return img

    def __len__(self):
        return len(self.data_files)

if __name__ == "__main__":

    dataset = Dataset(os.getcwd(), "faces", 100)
    loader = torch.utils.data.DataLoader(dataset, batch_size=10,
                                         shuffle=True, num_workers=4)
    for i, inp in enumerate(loader):
        print(i, inp.size())
