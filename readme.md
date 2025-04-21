# End-to-End Machine Learning

## Overview

Welcome to the **ML Model Deployment for Student Performance Prediction using AWS & CI/CD** project! This repository contains comprehensive resources and code for building, training, and deploying machine learning models.

## Features

- **Data Preprocessing**: Scripts for cleaning and preparing raw data for analysis.
- **Feature Engineering**: Tools to create and select the best features for your model.
- **Model Training**: Code to train machine learning models on processed data.
- **Model Evaluation**: Scripts to evaluate the performance of trained models.
- **Model Deployment**: Tools to deploy trained models for production use.

## How It Works

This project aims to provide a complete pipeline for machine learning projects, from data preprocessing to model deployment. It is designed to be a hands-on resource for both beginners and experienced practitioners in the field of machine learning.

## Getting Started

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/theanindya/end_to_end_machine_learning.git
cd end_to_end_machine_learning
pip install -r requirements.txt
```

## Installation

Ensure you have Python and pip installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The project includes a series of Python scripts that guide you through the entire machine learning pipeline. Each script focuses on a specific aspect of the pipeline:

1. **Data Preprocessing**
2. **Feature Engineering**: 
3. **Model Training**
4. **Model Evaluation**
5. **Model Deployment**


## Deployment

### Azure Deployment

The repository includes a GitHub Actions workflow for deploying the application to **Azure Web Apps**. The workflow file is located at:

```
.github/workflows/main_scoreprediction.yml
```

To set up Azure deployment:

1. **Azure Web App Setup**  
   Create an Azure Web App service to host your application.

2. **Configure Secrets**  
   In your GitHub repository, navigate to `Settings > Secrets and variables > Actions` and add the following secrets:
   - `AZURE_WEBAPP_NAME`: The name of your Azure Web App.
   - `AZURE_WEBAPP_PUBLISH_PROFILE`: The publish profile credentials of your Azure Web App.

3. **Trigger Deployment**  
   Push changes to the `main` branch or manually trigger the workflow to deploy the application to Azure.

> The GitHub Actions workflow automates the deployment process, ensuring that your application is up-to-date with the latest changes.

---

### AWS Deployment

To deploy this application to **AWS Elastic Beanstalk**, follow these steps:

1. **Install the AWS Elastic Beanstalk CLI**  
   Ensure that you have the [Elastic Beanstalk CLI (EB CLI)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html) installed on your machine.

2. **Initialize Elastic Beanstalk**  
   In the root directory of the project, run:

   ```bash
   eb init -p python-3.7 your-app-name
   ```

   Replace `your-app-name` with your desired application name. This command initializes your Elastic Beanstalk application and sets the Python version.

3. **Create an Environment and Deploy**  
   Run the following command to create an environment and deploy the application:

   ```bash
   eb create your-environment-name
   ```

   Replace `your-environment-name` with your desired environment name.

4. **Open the Application in a Browser**  
   After deployment, you can launch your deployed application with:

   ```bash
   eb open
   ```

> **Note:** Ensure that your AWS credentials are configured correctly on your machine to allow the EB CLI to interact with your AWS account.

By following these steps, you can deploy the application from the `end_to_end_machine_learning` repository to AWS Elastic Beanstalk.

