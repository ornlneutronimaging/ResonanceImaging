import ipywidgets as widgets
import numpy as np
from IPython.display import display


class Normalization(object):

	def __init__(self, sample=[], ob=[]):
		self.sample = sample
		self.ob = ob
		self.normalized =[]

	def run(self):
		"""Perform the normalization by doing sample/ob for each image _index"""

		w = widgets.IntProgress()
		w.max = len(self.sample)
		display(w)

    
		for _index in np.arange(len(self.sample)):
			_sample = self.sample[_index]
			_ob = self.ob[_index]
			_ob[_ob == 0] = np.NaN
			_norm = np.divide(_sample, _ob)
			_norm[np.isnan(_norm)] = 0
			_norm[np.isinf(_norm)] = 0
			self.normalized.append(_norm)

			w.value = _index+1

