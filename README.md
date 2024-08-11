# FastAPI GraphQL PostgreSQL

## Overview

This project demonstrates how to build a GraphQL API using FastAPI and Strawberry, interfacing with a PostgreSQL database. It includes a basic setup for querying and mutating user data.

## Setup

### Prerequisites

Ensure you have Docker, Google Cloud SDK, and Python 3.10+ installed.

### Install Dependencies

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd fastapi-graphql-postgres
    ```

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Environment Configuration

1. Create a `.env` file in the project root directory with the following content:
    ```plaintext
    DATABASE_URL=postgresql+asyncpg://gopal:gopal@localhost/fastapi-graphql-postgres
    ```

### Running the Application

1. Start the application locally:
    ```bash
    uvicorn app.main:app --reload
    ```

2. Access the GraphQL API at `http://localhost:8000/graphql`.

## GraphQL Endpoints

### Query

- **Endpoint:** `/graphql`
- **Example Query:**
    ```graphql
    query {
      users(page: 1, pageSize: 10, name: "John") {
        id
        name
        email
        isActive
        createdAt
        updatedAt
      }
    }
    ```

### Mutation

- **Endpoint:** `/graphql`
- **Example Mutation:**
    ```graphql
    mutation {
      createUser(name: "Jane Doe", email: "jane@example.com") {
        id
        name
        email
        isActive
        createdAt
        updatedAt
      }
    }
    ```

## CI/CD

The project is configured with GitHub Actions for automated testing, building, and deploying to Google Cloud Run.

### GitHub Actions Workflow

1. **Build Docker Image:**
    ```bash
    docker build -t fastapi-graphql-postgres .
    ```

2. **Push Docker Image to Google Container Registry:**
    ```bash
    gcloud builds submit --tag gcr.io/$PROJECT_ID/fastapi-graphql-postgres
    ```

3. **Deploy to Google Cloud Run:**
    ```bash
    gcloud run deploy fastapi-graphql-postgres \
      --image gcr.io/$PROJECT_ID/fastapi-graphql-postgres \
      --platform managed \
      --region $REGION
    ```

4. **Verify Deployment:**

    Access the deployed application at the provided URL and test the GraphQL endpoints.

## Troubleshooting

- Ensure that PostgreSQL is running and accessible with the credentials provided in the `.env` file.
- If you encounter errors during deployment, check the build and deployment logs for details.
