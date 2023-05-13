import inspect
import time
import numpy as np
import torch
from torch import nn
from d2l import torch as d2l


class HyperParameters: 
    """the base class of hyperparameters"""
    def save_hyperparameters(self, ignore=[]):
        """Save funciton argument into class attributes"""
        frame = inspect.currentframe.f_back
        _, _, _, local_vars = inspect.getargvalues(frame)
        self.hparams = {k:v for k, v in local_vars.items()
                            if k not in set(ignore+['self']) and not k.startswith('_')} 
        for k, v in self.hparams.items():
            setattr(self, k, v)