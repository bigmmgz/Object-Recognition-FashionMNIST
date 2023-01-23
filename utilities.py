from torch.utils.data import random_split


# Define data split function
def split_data(dataset, split):
  tr_va = []
  for frac in split:
      actual_count = frac * len(dataset)
      actual_count = round(actual_count)
      tr_va.append(actual_count)

  return random_split(dataset, tr_va)