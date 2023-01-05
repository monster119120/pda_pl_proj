import os
import math
import shutil
import numpy as np
from pathlib import Path
from .folder import DomainFolder

domains_list_str = 'brightness  contrast  defocus_blur  elastic_transform  fog  frost  gaussian_blur  impulse_noise  pixelate  saturate  shot_noise  snow  spatter  speckle_noise'
domains_list = domains_list_str.split()
domains_list = ['fog', 'frost', 'snow', 'clean']

class ImageNet_C(DomainFolder):
    all_domains = {}
    for d in domains_list:
        all_domains[d] = d
    # all_domains = {
    #             #    'gaussian_noise': 'gaussian_noise',
    #                'shot_noise': 'shot_noise',
    #                'impulse_noise': 'impulse_noise',
    #                'defocus_blur': 'defocus_blur',
    #             #    'glass_blur': 'glass_blur',
    #             #    'motion_blur': 'motion_blur',
    #             #    'zoom_blur': 'zoom_blur',
    #             #    'snow': 'snow',
    #                }

    all_splits = {'train': 'train',
                  'val': 'val'
                  }

    dataset_size = {}
    for d in domains_list:
        dataset_size[d] = {'train': 1281167, 'val': 50000}
    # dataset_size = {
    #                 # 'gaussian_noise': {'train': 1281167, 'val': 50000},
    #                 'shot_noise': {'train': 1281167, 'val': 50000},
    #                 'impulse_noise': {'train': 1281167, 'val': 50000},
    #                 'defocus_blur': {'train': 1281167, 'val': 50000},
    #                 # 'glass_blur': {'train': 1281167, 'val': 50000},
    #                 # 'motion_blur': {'train': 1281167, 'val': 50000},
    #                 # 'zoom_blur': {'train': 1281167, 'val': 50000},
    #                 # 'snow': {'train': 1281167, 'val': 50000},
    #                 }

    def __init__(self, root, splits, transform=None, target_transform=None, download=False):

        root = root

        domains = list(ImageNet_C.all_domains.keys())

        if 'test' in splits:
            splits.remove('test')
            splits.add('val')

        super(ImageNet_C, self).__init__(root=root,
                                         domains=domains,
                                         splits=splits,
                                         transform=transform,
                                         target_transform=target_transform,
                                         download=download)
    def download_data(self):
        print('imagenet_c cannot be downloaded, please generate first!')
        exit(0)