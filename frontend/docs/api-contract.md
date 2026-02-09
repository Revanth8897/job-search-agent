# API Contract (Draft)

## Auth
POST /api/auth/register
Body: { name, email, password }
Returns: { token, user }

POST /api/auth/login
Body: { email, password }
Returns: { token, user }

GET /api/auth/me
Headers: Authorization: Bearer <token>
Returns: { user }

## Jobs (Week 2+)
GET /api/jobs
POST /api/jobs
GET /api/jobs/:id
PUT /api/jobs/:id
DELETE /api/jobs/:id
