#use alpine linux and nginx as a non-root user
FROM nginxinc/nginx-unprivileged:alpine

#copy index file into the container
COPY index.html /usr/share/nginx/html

#expose ports listening to the server
EXPOSE 8080:80
