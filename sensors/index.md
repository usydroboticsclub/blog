# A list of Robotics sensors
Sorted roughly by how often you'll see them being used in robotics.


## GPS
- GPS stands for Global Positioning Satellite, but is not limited to the American GPS system.
    - Other GPS systems exist and are sometimes used in robotics, including GLONASS (Russian), QZSS(Japan), and Beidou (Chinese).
- GPS sensors provide positional information.
- The setup of a GPS sensor has an effect on its accuracy.
    - GPS sensors for boats often have a pair of antennae separated by around 2 metres, to obtain two sets of timings for better accuracy.
- The environment of a GPS sensor has an effect on its accuracy.
    - When there are tall metal buildings in a line (think New york, Tokyo or Sydney CBD), GPS signals can bounce off the buildings, creating echos that make it particularly difficult to get an accurate reading.
## Camera
- Subsets include stereo cameras and single wire FPV cameras.
## Motor encoders

## Lidar and radar

## Sensors that aren't particularly useful
Don't worry too much about memorising this list. As long as you're comfortable with using analogue measurements or I2C and reading datasheets, you'll be right.
- Human interface sensors
    - Capacitive touch sensors
- Specific analogue environment sensors
    - Temperature sensors
    - Hall effect sensors
- Reed switches