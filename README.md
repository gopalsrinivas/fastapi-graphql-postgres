# FastAPI GraphQL PostgreSQL

## Overview

This project demonstrates how to build a GraphQL API using FastAPI and Strawberry, interfacing with a PostgreSQL database.

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Set up environment variables in a `.env` file:
    ```plaintext
    DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
    ```

3. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

## GraphQL Endpoints

- Query: `/graphql`
- Mutation: `/graphql`

## CI/CD

Configured with GitHub Actions for building and deploying to Google Cloud Run.
