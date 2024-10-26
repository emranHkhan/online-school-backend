# Educational System API Documentation

## Table of Contents
- [Overview](#overview)
- [Base URL](#base-url)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
  - [Users API](#users-api)
  - [Departments API](#departments-api)
  - [Enrollments API](#enrollments-api)
  - [Comments API](#comments-api)
  - [Courses API](#courses-api)

## Overview
This API provides endpoints for managing an educational system, including user management, course administration, department organization, enrollment processing, and commenting functionality.

## Base URL
```
https://ondelivery-backend.vercel.app/api/
```

## Authentication
The API uses Django's authentication system. Authentication is required for most endpoints.

To authenticate requests, include the token in the header:
```
Authorization: Token <your-token>
```

## API Endpoints

### Users API
Base path: `/api/users/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/register/` | POST | Register a new user |
| `/login/` | POST | User login |
| `/profile/` | GET | Get user profile |
| `/profile/update/` | PUT | Update user profile |
| `/password/change/` | POST | Change password |

#### Example User Registration Request
```http
POST /api/users/register/
Content-Type: application/json

{
    "username": "student1",
    "email": "student@university.edu",
    "password": "secure_password",
    "role": "student"
}
```

### Departments API
Base path: `/api/departments/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | List all departments |
| `/` | POST | Create new department |
| `/<id>/` | GET | Get department details |
| `/<id>/` | PUT | Update department |
| `/<id>/courses/` | GET | List courses in department |
| `/<id>/faculty/` | GET | List faculty in department |

#### Example Department Creation
```http
POST /api/departments/
Content-Type: application/json
Authorization: Token <your-token>

{
    "name": "Computer Science",
    "code": "CS",
    "description": "Department of Computer Science",
    "head_of_department": "prof_user_id"
}
```

### Enrollments API
Base path: `/api/enrollments/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | List user enrollments |
| `/` | POST | Create new enrollment |
| `/<id>/` | GET | Get enrollment details |
| `/<id>/` | PUT | Update enrollment status |
| `/courses/<course_id>/students/` | GET | List enrolled students |
| `/student/<student_id>/courses/` | GET | List student's courses |

#### Example Enrollment Creation
```http
POST /api/enrollments/
Content-Type: application/json
Authorization: Token <your-token>

{
    "student_id": "student_user_id",
    "course_id": "course_id",
    "semester": "Fall 2024"
}
```

### Comments API
Base path: `/api/comments/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | List all comments |
| `/` | POST | Create new comment |
| `/<id>/` | GET | Get comment details |
| `/<id>/` | PUT | Update comment |
| `/<id>/` | DELETE | Delete comment |
| `/course/<course_id>/` | GET | Get course comments |

#### Example Comment Creation
```http
POST /api/comments/
Content-Type: application/json
Authorization: Token <your-token>

{
    "course_id": "course_id",
    "content": "Great course material!",
    "parent_comment_id": null
}
```

### Courses API
Base path: `/api/courses/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | List all courses |
| `/` | POST | Create new course |
| `/<id>/` | GET | Get course details |
| `/<id>/` | PUT | Update course |
| `/<id>/materials/` | GET | Get course materials |
| `/<id>/schedule/` | GET | Get course schedule |
| `/search/` | GET | Search courses |

#### Example Course Creation
```http
POST /api/courses/
Content-Type: application/json
Authorization: Token <your-token>

{
    "title": "Introduction to Programming",
    "code": "CS101",
    "department_id": "dept_id",
    "instructor_id": "instructor_user_id",
    "credits": 3,
    "capacity": 30,
    "description": "Basic programming concepts using Python"
}
```

## Response Formats

### Success Response
```json
{
    "status": "success",
    "data": {
        // Response data here
    }
}
```

### Error Response
```json
{
    "status": "error",
    "message": "Error description",
    "code": "ERROR_CODE"
}
```

## Error Codes
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 422: Validation Error
- 500: Internal Server Error

