# Google Cloud Run and GitHub Actions Deployment

This repository contains the implementation and deployment of three types of endpoints on Google Cloud Run, along with GitHub Actions for automated deployment and environment management.

## Task Overview

### 1. Create and Deploy Endpoints to Google Cloud Run

#### a) HTTPS Trigger
- **Endpoint**: Handles HTTPS requests.
- **Functionality**: Prints the details of the HTTPS request when triggered.

#### b) Firestore Trigger
- **Endpoint**: Handles events from Firestore.
- **Functionality**: Prints the details of the Firestore event when triggered by changes in a Firestore collection.

#### c) Scheduler Trigger
- **Endpoint**: Handles scheduled jobs from Google Cloud Scheduler.
- **Functionality**: Prints the details of the scheduled job when triggered.

### 2. Create a GitHub Action for Deployment to Google Container Registry (GCR)

- **Action**: Automates the deployment of code to Google Container Registry.
- **Functionality**: Builds, tags, and pushes Docker images to GCR.

### 3. Create a GitHub Action to Add a New GCP Project as a GitHub Environment

- **Action**: Facilitates the addition of a new GCP project as a GitHub environment.
- **Functionality**: Creates a new GitHub environment with the specified name and sets up the necessary GitHub secrets/variables for deployment.

## Deployment Instructions

### Deploy Endpoints to Google Cloud Run

1. **HTTPS Trigger Endpoint**

   - Navigate to `https_trigger/` folder.
   - Ensure the `Dockerfile` and `https_trigger.py` are correctly set up.
   - Deploy using GitHub Actions workflow defined in `.github/workflows/deploy-cloud-run.yml`.

2. **Firestore Trigger Endpoint**

   - Navigate to `firestore_trigger/` folder.
   - Ensure the `Dockerfile` and `firestore_trigger.py` are correctly set up.
   - Deploy using GitHub Actions workflow defined in `.github/workflows/deploy-cloud-run.yml`.

3. **Scheduler Trigger Endpoint**

   - Navigate to `scheduler_trigger/` folder.
   - Ensure the `Dockerfile` and `scheduler_trigger.py` are correctly set up.
   - Deploy using GitHub Actions workflow defined in `.github/workflows/deploy-cloud-run.yml`.

### GitHub Actions

1. **Deployment to Google Container Registry (GCR)**

   - **File**: `.github/workflows/deploy-to-gcr.yml`
   - **Function**: Builds and pushes Docker images to Google Container Registry.
   - **Usage**: Automatically triggered on push to the repository.

2. **Add all endpoints that are in the repository in GC**

 - **File**: `.github/workflows/deploy-cloud-run.yml`
 - **Feature**: adding all endpoints to Google Cloud and deployment in cloud run.
 - **Usage**: Starts automatically when any changes are made to files with endpoints
