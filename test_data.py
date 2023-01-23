import unittest
from torchvision import datasets
from torch.utils.data import random_split
from utilities import split_data


# Download and load the data
train_data = datasets.FashionMNIST('/content/MNIST_data/', 
                                    download = True, 
                                    train = True, 
                                  )


class TestData(unittest.TestCase):
  def test_split(self):
    # We know that len of train_data is 60,000
    ts, vs = split_data(train_data, [0.9, 0.1])
    self.assertEquals(len(ts), 54000)
    self.assertEquals(len(vs), 6000)