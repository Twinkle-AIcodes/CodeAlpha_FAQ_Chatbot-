# CodeAlpha FAQ Chatbot

## Project Overview

This project is a simple FAQ Chatbot developed using Python. It answers user questions by matching them with the most similar question stored in a FAQ database. The chatbot uses Natural Language Processing (NLP) techniques for text preprocessing and Cosine Similarity for question matching.

## Features

* Stores FAQs and their answers.
* Preprocesses text using NLTK.
* Uses TF-IDF Vectorization for text representation.
* Uses Cosine Similarity to find the best matching question.
* Provides the most relevant answer to the user.
* Simple command-line chat interface.
* Easy to run and understand for beginners.

## Technologies Used

* Python
* NLTK
* Scikit-learn

## Environment Setup

Create a Conda Environment:    conda create -n faqbot python=3.11

Activate the Environment:      conda activate faqbot

Install Required Libraries:    pip install nltk scikit-learn

## How to Run

Run the chatbot using:  python CODE2.py

## Example

========================================
        FAQ CHATBOT
Type 'exit' to quit
========================================

You: What is Python?
Chatbot: Python is a programming language.

You: What is AI?
Chatbot: AI stands for Artificial Intelligence.

You: exit
Chatbot: Goodbye!

## Project Objective

The objective of this project is to build a chatbot that can answer frequently asked questions by:

* Collecting FAQs and answers.
* Preprocessing text using NLP techniques.
* Matching user questions with stored FAQs using Cosine Similarity.
* Returning the best matching answer.
* Providing a simple chatbot interface for user interaction.

## Author

Developed as part of the CodeAlpha Internship Program,
Twinkle