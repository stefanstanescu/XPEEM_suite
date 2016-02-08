# XPEEM_suite
PyQtgraph-based image reducer for XPEEM data from HERMES beamline at SOLEIL synchrotron facility. Data are in NeXuS format. Images are drfit
corrected using the 'register_translation' function from the 'skimage' module. Multiprocessing is implemented using Pool method in order to efficiently 
calculate the drift correction. Several tests were done introducing in the processing different filters, like ndimage.sobel or hystogram equalization.
The calculations are done with none of the filters, but by applying a windowing on the rectangular ROI. Due to some issues between Qt and Multiprocessing
the calculation are made in separate Python sessions, outside the Qt interface. Images and TXT files are saved in the PROCESSING DIRECTORY to be
set at the beginning.
