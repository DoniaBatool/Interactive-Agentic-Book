# API Contracts – Feature 013: Auth & Personalization

## Endpoint: POST /auth/signup

### Request

```json
{
  "email": "user@example.com",
  "password": "securepassword123",
  "name": "John Doe",
  "profile": {
    "software_level": "intermediate",
    "hardware_level": "some",
    "technologies": {
      "python": true,
      "ros2": true,
      "gazebo": false,
      "isaac": false,
      "aiMl": true,
      "unity": false,
      "linux": true,
      "docker": true
    },
    "learning_goals": "I want to learn robotics and build autonomous systems"
  }
}
```

### Response (Success - 201)

```json
{
  "user": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe",
    "profile": {
      "software_level": "intermediate",
      "hardware_level": "some",
      "technologies": {
        "python": true,
        "ros2": true,
        "aiMl": true,
        "linux": true,
        "docker": true
      },
      "learning_goals": "I want to learn robotics and build autonomous systems"
    }
  },
  "message": "Account created successfully"
}
```

### Response (Error - 400)

```json
{
  "detail": "Email already registered"
}
```

---

## Endpoint: POST /auth/signin

### Request

```json
{
  "email": "user@example.com",
  "password": "securepassword123",
  "remember_me": true
}
```

### Response (Success - 200)

Sets httpOnly cookie: `session_token`

```json
{
  "user": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe",
    "profile": {
      "software_level": "intermediate",
      "hardware_level": "some",
      "technologies": {"python": true, "ros2": true}
    }
  },
  "message": "Signed in successfully"
}
```

### Response (Error - 401)

```json
{
  "detail": "Invalid email or password"
}
```

---

## Endpoint: POST /auth/signout

### Request

No body required. Session token from cookie.

### Response (Success - 200)

Clears httpOnly cookie: `session_token`

```json
{
  "message": "Signed out successfully"
}
```

---

## Endpoint: GET /auth/session

### Request

Session token from cookie (automatic).

### Response (Authenticated - 200)

```json
{
  "authenticated": true,
  "user": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe",
    "profile": {
      "software_level": "intermediate",
      "hardware_level": "some",
      "technologies": {"python": true, "ros2": true}
    }
  }
}
```

### Response (Not Authenticated - 200)

```json
{
  "authenticated": false,
  "user": null
}
```

---

## Endpoint: GET /auth/profile

### Request

Session token from cookie (required).

### Response (Success - 200)

```json
{
  "software_level": "intermediate",
  "hardware_level": "some",
  "technologies": {
    "python": true,
    "ros2": true,
    "gazebo": false,
    "isaac": false,
    "aiMl": true,
    "unity": false,
    "linux": true,
    "docker": true
  },
  "learning_goals": "I want to learn robotics and build autonomous systems"
}
```

---

## Endpoint: PUT /auth/profile

### Request

Session token from cookie (required).

```json
{
  "software_level": "advanced",
  "technologies": {
    "python": true,
    "ros2": true,
    "gazebo": true,
    "isaac": true
  },
  "learning_goals": "Building autonomous humanoid robots"
}
```

### Response (Success - 200)

```json
{
  "software_level": "advanced",
  "hardware_level": "some",
  "technologies": {
    "python": true,
    "ros2": true,
    "gazebo": true,
    "isaac": true,
    "aiMl": true,
    "linux": true,
    "docker": true
  },
  "learning_goals": "Building autonomous humanoid robots"
}
```

---

## Cookie Settings

```
Set-Cookie: session_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...; 
  HttpOnly; 
  Secure; 
  SameSite=Lax; 
  Max-Age=604800; 
  Path=/
```

## JWT Token Payload

```json
{
  "sub": "1",
  "email": "user@example.com",
  "exp": 1735689600,
  "iat": 1735084800,
  "type": "session"
}
```

