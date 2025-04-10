# API Integration Guide

## Step 1: Authentication
- Use OAuth2 or API key to authenticate with your endpoint.

## Step 2: Send Inference Request
```bash
curl -X POST https://yourdomain.com/inference \
     -H 'Authorization: Bearer <TOKEN>' \
     -d '{"input": "example text"}'
```

## Step 3: Handle the Response
- Parse JSON result, extract confidence scores, and log responses for QA.
