# Stage 1: Build React app
FROM node:14 AS build-frontend

WORKDIR /frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend ./
RUN npm run build

# Stage 2: Build Flask app
FROM python:3.10 AS build-backend

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend .

# Stage 3: Final stage to combine everything
FROM python:3.10

WORKDIR /app

# Copy Flask app from build-backend stage
COPY --from=build-backend /app /app

# Copy React build from build-frontend stage
COPY --from=build-frontend /frontend/build /app/static

# Install Redis server
RUN apt-get update && apt-get install -y redis-server

# Expose ports
EXPOSE 5000

# Command to run Redis server and Flask app
CMD service redis-server start && flask run --host=0.0.0.0
