# Magnetometer-Neptune
Analyse the Magnetometer data captured with Voyager 2 of Neptune.


## Current updates
### MATLAB
* Plot imported data

### PYTHON
* read data
* clean data (999.99)


## Data
The data is by NASA:
* Voyager 2, Magnetometer, Neptune, Version 1.0

Download dataset here:
* https://pds-ppi.igpp.ucla.edu/search/view/?id=pds://PPI/VG2-N-MAG-4-RDR-HGCOORDS-1.92SEC-V1.0

Information about the dataset: 
* https://pds.nasa.gov/ds-view/pds/viewProfile.jsp?dsid=VG2-N-MAG-4-RDR-HGCOORDS-1.92SEC-V1.0

## Feature extraction:
"For time-series data the standard method is bag-of-frames, chopping it up into small chunks called frames. The frames can be overlapped and windowed or disjoint. Frame size is an important hyper-parameter and depends on task. Features like min,max,median,variance,RMS are calculated on each frame. To use variation over time in the classifier one uses lagged or delta features. Lagged features are values from the frames before. Delta features are computed as the difference of current frame to the previous one."
* https://stackoverflow.com/questions/50519856/how-do-i-apply-machine-learning-classification-methods-to-1d-time-series-data/50520507
