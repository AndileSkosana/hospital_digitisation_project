# Use the official PostgreSQL image
FROM postgres:13

# Copy the init SQL file to create the necessary tables
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the port for PostgreSQL
EXPOSE 5432
