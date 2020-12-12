# Agile Principles

## Setup

This setup uses docker

1. Create a .env file with the needed environment variables. A sample file named `example.env` is provided as a reference.
2. In `db.sql` line 2, change the names of the database and user into the ones specified in your .env file. If your database is named `database` and your user is named `user`, then replace `GRANT ALL PRIVILEGES ON test_default.* TO 'default'@'%';` with `GRANT ALL PRIVILEGES ON test_database.* TO 'user'@'%';`
3. Run `nps run` or `docker-compose up` to start all the docker containers.