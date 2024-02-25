# This Dockerfile is used to build a Docker image for a PostgreSQL database.
# It extends the official postgres:latest image and sets up the necessary environment variables.

# The environment variables POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_PORT, and DB_HOST are used to configure the PostgreSQL instance.

# The db/init.sql script is added to the /docker-entrypoint-initdb.d/ directory, which will be executed when the container starts.

FROM postgres:latest

# ARG POSTGRES_USER
# ARG POSTGRES_PASSWORD
# ARG POSTGRES_DB
# ARG POSTGRES_PORT
# ARG DB_HOST

# ENV POSTGRES_USER=$POSTGRES_USER
# ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
# ENV POSTGRES_DB=$POSTGRES_DB
# ENV POSTGRES_PORT=$POSTGRES_PORT
# ENV DB_HOST=$DB_HOST
 

ENV POSTGRES_USER=5432
ENV POSTGRES_PASSWORD=pguser
ENV POSTGRES_DB=pgpassword!123
ENV POSTGRES_PORT=5432
ENV DB_HOST=localhost

# Add SQL script to Docker image
ADD db/init.sql /docker-entrypoint-initdb.d/