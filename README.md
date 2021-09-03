# Pick.a.chair: A ReverseImage Search Engine built with deep learning
[Bahar Biazar](https://www.linkedin.com/in/bahar-biazar/)  
September 2021
App Link: http://13.57.194.193:5000/

## Table of Contents
* [Overview and Motivation](#overview-and-motivation)
* [Methodology](#methodology)
* [Tools and Technologies](#tools-and-technologies)
* [Acknowledgments](#acknowledgments)

## Overview and Motivation
- For this project, my motivation was to develop a recommendation tool that could take a user-uploaded image of furniture and return images of fine art, along with relevant information about the piece, that are most visually similar. 

## Methodology 
Implementation of this project involved: 

- Build a corpus of 20,000+ images and metadata scraped from wayfair.com

- Use transefer learning to predict the similarities. 

- Develop a Flask web application that allows user to upload an image of furniture from their computer. Return the top 30 pieces of fine art that the model determines are the best matches.

## Tools and Technologies
- Key python libraries:  
      a. Pandas (Metadata cleaning and manipulation)  
      b. BeautifulSoup, Selenuim (Image and metadata scraping)  
      c. Tensorflow, Keras (Vgg16 model)

- AWS EC2 (Data storage and App deployment)

- Flask (Web framework for app)

## Acknowledgments
- Special thanks to amazing Galvanize people specially Noah and Ryan.



