from __code import image_processing, gui_widgets, file_handler
import numpy as np

from IPython.display import display
from ipywidgets import widgets
from IPython.core.display import HTML
import glob
import os


class Loading(object):
    
    data = []
    list_sample_images = []
    
    def __init__(self, working_dir='', message='Select the Sample Folder!'):
        self.working_dir = working_dir
        self.message = message
        
    def run(self):
        display(HTML('<span style="font-size: 20px; color:blue">' + self.message + '</span>'))
        sample_image = gui_widgets.gui_dname(dir=self.working_dir)
        list_sample_images = np.sort(glob.glob(os.path.join(sample_image, '*.fits')))

        if len(list_sample_images) > 0:
    
            w = widgets.IntProgress()
            w.max = len(list_sample_images)
            display(w)

            _data = []
            for _index, _file in enumerate(list_sample_images):
                _image = np.array(file_handler.load_data(_file), dtype=float)
                _image = image_processing.single_gamma_filtering(_image)
                _image[_image == np.inf] = 0 # removing inf values
                _image[np.isnan(_image)] = 0
                _data.append(_image)
                w.value = _index + 1

            [nbr_files, height, width] = np.shape(_data)
            _data = np.squeeze(_data)

            self.data = _data
            self.list_sample_images = list_sample_images