# Fire Detection & Prediction System (AI + FastAPI + Streamlit + AWS Serverless)

## Overview

This project is an **end-to-end intelligent fire detection and prediction system** designed to identify potential fire hazards using sensor data and machine learning. It integrates **AI, backend APIs, interactive dashboards, and cloud-based serverless architecture** to provide a scalable and real-time solution.

The system takes input from environmental sensors such as **temperature, gas, smoke, and flame**, processes the data using a trained machine learning model, and predicts whether there is a fire risk.

To ensure scalability and reliability, the application leverages **AWS serverless services including AWS Lambda, API Gateway, and DynamoDB**, eliminating the need for traditional server management.

## System Architecture Overview

1. **Frontend (Streamlit Dashboard)**

   * Provides a user-friendly interface
   * Allows users to input sensor values
   * Displays predictions and visual graphs

2. **Backend (FastAPI / AWS Lambda)**

   * Handles API requests
   * Processes input data
   * Runs machine learning prediction

3. **Machine Learning Model (Scikit-learn)**

   * Trained using historical sensor data
   * Uses **Random Forest Classifier**
   * Predicts fire risk

4. **Cloud Layer (AWS Serverless)**

   * **API Gateway** → exposes REST endpoints
   * **Lambda** → executes prediction logic
   * **DynamoDB** → stores sensor data & predictions

## Workflow

1. User enters sensor values in the dashboard
2. Frontend sends request to API (FastAPI or AWS API Gateway)
3. Backend/Lambda processes the request
4. ML model predicts fire risk
5. Result is stored in DynamoDB
6. Response is sent back and displayed on UI

## Key Functionalities

* Real-time fire prediction
* Data visualization (graphs for each sensor)
* Cloud-based serverless execution
* Data storage and retrieval using DynamoDB
* API-based communication between components

## AWS Integration 

This project uses a **serverless cloud architecture**, which provides:

* **AWS Lambda** → Executes backend logic without managing servers
* **AWS API Gateway** → Provides secure and scalable API endpoints
* **AWS DynamoDB** → Stores prediction data with high performance

## Why Serverless?
* No server maintenance
* Automatic scaling
* Cost-efficient (pay per use)
* High availability

## Machine Learning Approach

* Dataset includes sensor readings:
  * Temperature
  * Gas
  * Smoke
  * Flame
* Model used: **Random Forest Classifier**
* Trained using `scikit-learn`
* Model is saved as `.pkl` and reused for predictions

## Project Objective

The main goal of this project is to:

* Detect fire risks early using sensor data
* Build a scalable and intelligent monitoring system
* Demonstrate integration of **AI/ML + APIs + Cloud computing**

## Key Highlights
* Real-time prediction system
* Cloud-native architecture (AWS)
* Serverless deployment
* Clean modular code structure
  
## Learning Outcomes
Through this project, the following concepts were implemented:

* Machine Learning model development
* REST API creation using FastAPI
* Frontend dashboard using Streamlit
* AWS serverless services integration
* End-to-end system design

## Summary
This project showcases a **complete intelligent system** that combines **machine learning, backend APIs, frontend visualization, and AWS cloud services** to deliver a real-time fire prediction solution. It highlights practical implementation of modern technologies in building scalable and efficient applications.

