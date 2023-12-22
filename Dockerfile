# Stage 1: Building the React application
FROM node:14.15.4-alpine as build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy app source
COPY frontend/. .

# Build app
RUN npm run build

# Stage 2: Setting up Python with Nginx
FROM python:3.8-alpine

# Install Nginx and supervisord
RUN apk add --no-cache nginx supervisor

# Create a directory for storing the logs
RUN mkdir -p /var/log/supervisor

# Create a directory for the Flask app
WORKDIR /usr/src/app

# Copy the built React app
COPY --from=build /app/build /usr/share/nginx/html

# Copy the Flask app source
COPY backend /usr/src/app/

# Install Python dependencies
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

# Set up Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Set up supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports (80 for Nginx and whatever your Flask app uses)
EXPOSE 80
Expose 8080

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
