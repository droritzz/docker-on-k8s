#use alpine linux
FROM nginx:alpine

#copy index file into the container
COPY index.html /usr/share/nginx/html

#expose ports listening to the server
EXPOSE 8080:80
