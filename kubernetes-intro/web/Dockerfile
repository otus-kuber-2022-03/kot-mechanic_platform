FROM nginx

RUN mkdir /app
COPY index.html /app/
COPY homework.html /app/
ADD custom.conf /etc/nginx/conf.d/

EXPOSE 1001

CMD ["nginx", "-g", "daemon off;"]

