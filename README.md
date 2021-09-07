# Pick.a.chair: A Reverse Image Search Engine built with deep learning
[Bahar Biazar](https://www.linkedin.com/in/bahar-biazar/)  
September 2021
App Link: http://50.18.139.230:5000

## Table of Contents
* [Overview and Motivation](#overview-and-motivation)
* [Methodology](#methodology)
* [Tools and Technologies](#tools-and-technologies)
* [Acknowledgments](#acknowledgments)

## Overview and Motivation
- Prior to Galvanize, I worked in the interior design, architecture, and urban planning industry for a number of years, where I enjoyed creating spaces in the real world that people love. Although the outcome is pleasing, there are some aspects of the process that in my opinion are very time consuming and could be done faster and more efficient with more advanced tools. After learning about convolutional neural networks and computer vision algorithms, I decided to use my data science skills to make an app for reverse image search that could take a user-uploaded image of furniture and return visually similar items, along with relevant information about the pieces. This is not only useful for interior designers but also anyone who is shopping for furniture online can benefit from it.
<img src="http://www.nadjavilenne.com/wordpress/wp-content/uploads/2012/09/chaises_decoupees_opma.jpg" width="300 px" />

## Methodology 
Implementation of this project involved: 

- Building a corpus of 16,000+ images and metadata scraped from wayfair.com using Selenium and BeautifulSoup.
- Implementing a content based image retrival system(CBIR) that converts image data into numerical values and compares similarity between database and query image and returns similar items, using TensorFlow/Keras.
<img src = 'https://www.researchgate.net/profile/Mohammed-Elmogy/publication/273258916/figure/fig3/AS:669349706739729@1536596814668/A-typical-Content-Based-Image-Retrieval-system.png' width = '500'/>
- Using VGG16, a pre-trained CNN model as a feature extractor to convert images into number arrays. I used transfer learning,kept the convolutional layers and used the FC1 layer as the outcome. All the images in the database are converted to matricies, predicted by this layer and the extracted features are saved as arrays of numbers. Then a similarity measure is used to calculate the distance between these images and the quary image which is also processed throught the same model. I used euclidean distance but cosine similarity also returns the same results.
<img src = 'https://miro.medium.com/max/1400/1*ZqkQYVB3_Gw0hjrAMzi6_A.png' width = '700'/>
- Develop a Flask web application that allows user to upload an image of furniture from their computer and return the top 10 pieces of fine art that the model determines are the best matches. The app is put on a docker container to be deployed on AWS. You can see test results with a query image below:
![](images/query.png)

- Create an Amazon EC2 t2.large instance to host the docker container with a public IP which makes the app accessible to public.

![](images/app.png)

## Key Tools and Technologies
a. Pandas (Metadata cleaning and manipulation)  
b. BeautifulSoup, Selenuim (Image and metadata scraping)  
c. Tensorflow, Keras (Vgg16 model)<br>
d. Flask App, Docker, Amazon cloud compute system (Web app, data storage and deployment)

## Acknowledgments
- Special thanks to amazing Galvanize people specially Noah and Ryan.



