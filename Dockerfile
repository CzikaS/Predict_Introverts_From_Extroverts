# Use a lightweight, official Python 3.11 image as the base
FROM python:3.11-slim

# Set environment variables to optimize Python inside Docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system-level dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Install the core Python packages
RUN pip install --no-cache-dir \
    jupyterlab \
    matplotlib \
    seaborn \
    numpy \
    pandas \
    scikit-learn \
    imbalanced-learn \
    xgboost \
    catboost

# Expose the port that JupyterLab will run on
EXPOSE 8888

# Command to run when the container starts
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token='kaggle123'"]
