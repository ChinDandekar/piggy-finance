# base image
FROM node:14.15.4-alpine as build

# set working directory
WORKDIR /app

# copy package.json and package-lock.json
COPY frontend/package*.json ./

# install dependencies
RUN npm install

# copy app source
COPY frontend/. .

# build app
RUN npm run build

# production environment
FROM nginx:1.21.0-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]