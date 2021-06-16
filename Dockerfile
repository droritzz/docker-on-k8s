#use alpine linux and nginx as a non-root user
FROM nginxinc/nginx-unprivileged:alpine

#copy index file into the container
COPY index.html /usr/share/nginx/html

#expose ports listening to the server. unprivileged image uses port 8080 instead of 80 for nginx
EXPOSE 8090:8080
