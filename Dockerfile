ARG PYTHON_VERSION=3.8

# Stage 1: Build image with dependencies
FROM python:${PYTHON_VERSION} AS builder

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy only the dependencies file to take advantage of Docker cache
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Stage 2: Create the final image with only the necessary files
FROM python:${PYTHON_VERSION}-slim

WORKDIR /app

# Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python${PYTHON_VERSION}/site-packages /usr/local/lib/python${PYTHON_VERSION}/site-packages

# Copy the application code
COPY . .

# Expose the FastAPI port
EXPOSE 8080

# Command to run the application
CMD ["poetry", "run", "uvicorn", "psyncly:app", "--host", "0.0.0.0", "--port", "8080"]
