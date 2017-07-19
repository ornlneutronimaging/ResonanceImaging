from __code import image_processing, gui_widgets, file_handler
import numpy as np

from IPython.display import display
from ipywidgets import widgets
from IPython.core.display import HTML
import glob
import os


class ExportImages(object):
    
    data = []
    
    def __init__(self, working_dir=''):
        self.working_dir = working_dir
        
    def run(self, data_array=[], list_original_file_names=[]):
        display(HTML('<span style="font-size: 20px; color:blue">Select the Output Folder!</span>'))
        output_folder = gui_widgets.gui_dname(dir=self.working_dir)

        if output_folder == '':
            return

        w = widgets.IntProgress()
        w.max = len(list_original_file_names)
        display(w)

        _data = []
        for _index, _file in enumerate(list_original_file_names):
            _data = data_array[_index]
            _basename = os.path.basename(_file)
            _full_file_name = os.path.join(output_folder, _basename)  
            file_handler.save_data(_data, _full_file_name)

            w.value = _index + 1

