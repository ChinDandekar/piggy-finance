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
FROM python:3.10-alpine3.18

# Install Nginx and supervisord
RUN apk add --no-cache nginx supervisor

# Install GCC for package cffi (django-allauth dependency)
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev

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

# Make all migrations so sqlite3 db is set up to accept users
RUN python manage.py makemigrations
RUN python manage.py migrate

# Add Google app to Django for OAuth
RUN python manage.py addgoogleapp

# Register domain on Django
RUN python manage.py setdomain

# Add chinmay dandekar as super user
RUN python manage.py addsuperuser


# Set up Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Set up supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports (80 for Nginx and whatever your Flask app uses)
EXPOSE 80
EXPOSE 8080

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
