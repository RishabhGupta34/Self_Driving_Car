# Self Driving Car
Machine learning model for building Self Driving Cars using Behavioral Cloning. For generating the dataset and testing the model I have used the udacity self driving car simulator.

# Testing the Model
python run.py --path="path-to-model-file"

For eg: python run.py --path=modelv6_0.1730.h5

# Generating the Dataset
The dataset is generated using udacity self driving car simulator. It gives information about the steering angle,throttle and left,right,center images as seen from the front of the car.

# Preprocessing the Dataset
1. One out of the three images (left,right,center) is chosen at random from each sample of the dataset.

2. The image is flipped at random.

3. The angle is increased by 0.2 degree if the image chosen is left and decreased by 0.2 degree if the image chosen is right.

