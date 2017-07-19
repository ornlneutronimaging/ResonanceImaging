from __future__ import print_function

resonance_imaging = 'Resonance Imaging'

requirements = [
    'ipywidgets',
    'periodictable',
    'numpy',
    'glob',
    'pyfits',
    'PIL',
    'pickle',
    'shutil',
    'pyqtgraph',
    'scipy',
]

import_result = {p: False for p in requirements}

print("Checking requirements for {}".format(resonance_imaging))

for package in requirements:
    try:
        __import__(package)
        import_result[package] = True
    except ImportError:
        pass

success = all(import_result.values())

if success:
    print('All required packages installed, checking ipywidgets version...')
else:
    print('Please install these missing packages '
          'for the tutorial "{}":'.format(resonance_imaging))
    missing = [k for k, v in import_result.items() if not v]
    print('\t' + '\n\t'.join(missing))

import ipywidgets
ipywidgets_version = ipywidgets.__version__.startswith('7')

if not ipywidgets_version:
    print('Please upgrade ipywidgets to version 7 by running:')
    print('pip install --pre ipywidgets')
    print('jupyter nbextension enable --py widgetsnbextension')
else:
    print('ipywidgets version is good!')
