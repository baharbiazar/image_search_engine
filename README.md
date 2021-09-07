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
- Prior to Galvanize, I worked in the interior design, architecture, and urban planning industry for a number of years, where I enjoyed creating spaces in the real world that people love. Although the outcome is pleasing, there are some aspects of the process that in my opinion are very time consuming and could be done faster and more efficient with more advanced tools. After learning about convolutional neural networks and computer vision algorithms, I decided to use my data science skills to make an app for reverse image search that could take a user-uploaded image of furniture and return visually similar items, along with relevant information about the pieces. This is not only useful for interior designers but anyone who is shopping for furniture online can benefit from it.
<img src="http://www.nadjavilenne.com/wordpress/wp-content/uploads/2012/09/chaises_decoupees_opma.jpg" width="300" />
## Methodology 
Implementation of this project involved: 

- Building a corpus of 16,000+ images and metadata scraped from wayfair.com using Selenium and BeautifulSoup.
- Implementing a content based image retrival system(CBIR) that converts image data into numerical values and compares similarity between database and query image and returns similar items, using TensorFlow/Keras
- Using VGG16, a pre-trained CNN model as a feature extractor to convert images into number arrays. I used transfer learning to keep the convolutional layers and 


- Develop a Flask web application that allows user to upload an image of furniture from their computer. Return the top 30 pieces of fine art that the model determines are the best matches.

## Key Tools and Technologies
a. Pandas (Metadata cleaning and manipulation)  
b. BeautifulSoup, Selenuim (Image and metadata scraping)  
c. Tensorflow, Keras (Vgg16 model)
d. Flask App, Docker, Amazon cloud compute system (Web app, data storage and deployment)

## Acknowledgments
- Special thanks to amazing Galvanize people specially Noah and Ryan.



