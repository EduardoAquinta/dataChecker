# Data Format Checker

This repo is a simple tool to check whether ingested data is set out in the correct format

## Tech Spike

The primary goal is to spike various tech, including:
- python3
- PyCharm
- pandas 
- GCS Oauth2
- GCS Buckets
- GCS Cloud Functions
- GitHub Actions
-  .csv

## Functionality

The goal is to have an automated process that validates the format of any .csv files uploaded to an S3 bucket. 

Uploading will trigger a Lambda to run some data validation code against the .csv file. 

This will also utilise GitHub Actions for CI/CD controls that ensure consistency.

## Usage

Although this code has a fairly narrow use-case, it is free to be used/forked by anyone. It is all my own work. 

