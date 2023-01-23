# Object Recognition - Xiaohan Sun -s5321302


## Abstract
Image recognition is a technique that uses computers to process and analyse images in order to recognise various different patterns of pairs of images. The goal of this project is to apply neural networks to feature recognition of input clothing images and classify them based on the FashionMNIST dataset.


## Detailed Description
For this project, I will use convolutional neural networks to build image classification models. After several convolutions, pooling and activations, the data features are extracted. The output is then passed through a fully connected layer, completing the forward propagation process. Finally the parameters are updated in the backward propagation by calculating the loss between the predicted and true values. This step is repeated until a model with good recognition is trained, allowing the model to distinguish ten different categories of item images into their respective categories.


### Datasets
I will use the FashionMNIST dataset, a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 greyscale image associated with 10 categories of labels. The dataset can be found at: https://github.com/zalandoresearch/fashion-mnist


### Arcitecture Proposal
First I built a base neural network for training tests, on top of which I adjusted the parameters and built a larger and deeper convolutional neural network. The steps are divided into five main steps.
1. Input training samples and pre-process the data.
2. Build the convolutional neural network.
3. Set up the optimiser and calculate the loss function.
4. Update the parameters.
5. Evaluate the model.


## References
[1]Learning Multiple Layers of Features from Tiny Images，Alex Krizhevsky，2009

[2]Ming Liang, Xiaolin Hu; Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2015, pp. 3367-3375

[3]R. L. Galvez, A. A. Bandala, E. P. Dadios, R. R. P. Vicerra and J. M. Z. Maningo, "Object Detection Using Convolutional Neural Networks," TENCON 2018 - 2018 IEEE Region 10 Conference, 2018, pp. 2023-2027, doi: 10.1109/TENCON.2018.8650517.
