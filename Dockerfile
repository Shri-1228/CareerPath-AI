# 1. Use Python 3.11
FROM python:3.11-slim

# 2. Set the working directory to /app
WORKDIR /app

# 3. Copy EVERYTHING from your Space into the container
COPY . .

# 4. Install the libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. Tell Streamlit to run on port 7860 (Hugging Face default)
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]