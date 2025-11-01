# Idiotics_Google_GENAI_Hackathon
EyeSpy is an AI-powered fake news detector. It uses a Flask backend and a machine learning model to analyze text and identify misinformation, providing a confidence score through a simple web interface.The system leverages Natural Language Processing (NLP) with a TF-IDF vectorizer and a Logistic Regression model

# EyeSpy - AI-Powered Fake News Detection

A cutting-edge multimodal system for detecting fake news and manipulated content using artificial intelligence.

## Features

- **Text Analysis**: Advanced NLP algorithms detect linguistic patterns and misinformation indicators.
- **Image Forensics**: (Coming Soon) Computer vision techniques to identify digital manipulation and deepfakes.
- **Real-time Processing**: Lightning-fast analysis with confidence scores.
- **Modern UI**: Sleek, responsive frontend with dark theme.

## Backend Technology Stack

Here's a brief overview of the backend technologies and libraries used in EyeSpy:

- **Flask**: A lightweight web framework for Python used to build the core API that serves the fake news detection model.
- **Flask-CORS**: An extension for Flask that handles Cross-Origin Resource Sharing (CORS), making it possible for the frontend to communicate with the backend API.
- **scikit-learn**: A powerful and easy-to-use machine learning library for building, training, and deploying the fake news classification model.
- **Joblib**: A set of tools to provide lightweight pipelining in Python. In this project, it's used for saving and loading the trained scikit-learn model and vectorizer.
- **PyMongo**: The official Python driver for MongoDB, enabling the application to connect to and interact with the database for storing analysis results and training data.
- **Pandas**: A versatile data analysis and manipulation library, primarily used for loading and processing the datasets during the model training phase.
- **Numpy**: A fundamental package for scientific computing in Python, used by scikit-learn for numerical operations.
- **Pillow**: The Python Imaging Library fork, included for future development of image-based analysis and manipulation features.
- **Gunicorn**: A robust and production-ready web server (WSGI) for deploying the Flask application, ensuring scalability and performance.

## Key Components

- **Docker**: Simplifies the setup of the development environment by containerizing the MongoDB database. The `docker_setup.bat` script automates the process of starting the database container.
- **MongoDB**: A NoSQL database used to store the news articles dataset, analysis history, and other application data. The application is configured to connect to a local MongoDB instance, but also supports cloud-based MongoDB Atlas.
- **News Datasets**: The project includes `Fake.csv` and `True.csv` datasets, which are used to train the fake news detection model. These datasets are processed by the scripts in the `backend` folder.
- **Streamlit**: An open-source app framework for Machine Learning and Data Science projects. In EyeSpy, `modelrun.py` uses Streamlit to provide a simple and interactive interface for testing the trained model with custom text inputs.

## How to Run

### Prerequisites

- Docker
- Python 3

### Instructions

1.  **Start the backend and database:**

    Open a terminal and run the following command from the `EyeSpy/backend` directory:

    ```bash
    ./docker_setup.bat
    ```

    This will start a MongoDB container, set up the database, and run the Flask backend server.

2.  **Start the frontend:**

    Open another terminal and run the following command from the `EyeSpy/frontend` directory:

    ```bash
    python serve.py
    ```

    This will start a simple Python web server for the frontend.

3.  **Access the application:**

    Open your web browser and go to `http://localhost:8080`.

## File Structure

```
C:\USERS\SURAJ\DOWNLOADS\EYESPY\EYESPY

    architecture_diagram.md
    
+---backend

        app.py
        cloud_setup.py
        database.py
        database_extension.py
        dataset_loader.py
        docker_setup.bat
        fake_news_model.ipynb
        model.jb
        modelrun.py
        requirements.txt
        run_server.bat
        run_with_mongodb.bat
        setup_database.py
        vectorizer.jb
        
+---Datasets

        Fake.csv
        True_news.csv
        
+---frontend
        index.html
        serve.py
        test.html
```

## Testing the Model

To test only the model, you can run the `modelrun.py` file (with streamlit) after running the `fake_news_model.ipynb` file to generate the model and vectorizer files.

## Dependencies

- Flask
- Flask-CORS
- numpy
- scikit-learn
- joblib
- Pillow
- pymongo
- pandas
- gunicorn

All Python dependencies are listed in `backend/requirements.txt`.

## License

MIT License - Feel free to use and modify for your projects.
