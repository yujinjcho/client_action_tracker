# Client Metric Tracker

Backend service for collecting and service client metrics.

## Local setup

Requires postgres, dbmate and vercel.

- `dbmate up` to create database and run migrations locally.
- `vercel dev` to run app locally.

## Production

Python code deployed on vercel and database is provisioned by Supabase.

Run the following with actual config values to execute migrations in production.
```
# See migration status
DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/DATABASE?sslmode=disable" dbmate status
# Run migration
DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/DATABASE?sslmode=disable" dbmate up
```
