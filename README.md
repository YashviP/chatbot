# CHATBOT

# Introduction

Chatbots are “computer programs which conduct conversation through auditory or textual methods”.


# Approach 

Seq2Seq Model of RNN(Recurrent Neural Networks)

# Dataset Selection

When thinking about applying machine learning to any sort of task, one of the first things we need to do is consider the type of dataset that we would need to train the model. Here I created my own dataset.Some common datasets are the 'Cornell Movie Dialog Corpus' ,'the Ubuntu corpus' , and 'Microsoft’s Social Media Conversation Corpus' .

# DataPreProcessing 

A big part of machine learning involves dataset preprocessing.he data archives from each of these sources comes differently formatted, and contains parts that we don’t really need.Our goal,is to just create one unified file that contains pairs in the form of (MESSAGE, RESPONSE). 
 
$ python3 dataprenew.py


# Word Vector 

To generate word vectors, we use the classic approach of a Word2Vec model. The basic idea is that the model creates word vectors by looking at the context with which words appear in sentences. Words with similar contexts will be placed close together in the vector space.I trained the Word2Vec model , which saves the word vectors in a Numpy object.

$ python3 word2vec.py

# Creating Seq2Seq Model with Tensorflow 

https://www.tensorflow.org/tutorials

$ python3 seqmodel.py



# Testing Chatbot

$ python3 test.py









