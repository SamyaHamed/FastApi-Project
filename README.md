# FastApi Project 
This project is a backend web application built using FastAPI that provides a complete authentication and user management system.
The platform supports two main user roles: Trainees and Companies, where each user has a clear role and related profile data.

The system is designed with a clean architecture approach, separating concerns into controllers, services, models, and dependencies, making the codebase scalable, maintainable, and easy to extend.

## Tech Stack

- **Framework:** FastAPI
- **Database:** SQLite with SQLAlchemy ORM
- **Authentication:** JWT (JSON Web Tokens)
- **Password Hashing:** bcrypt
- **Validation:** Pydantic
- **Server:** Uvicorn



## Features

### Authentication

- User registration with separate flows for trainees and companies
- JWT-based login with 30-minute token expiration
- bcrypt password hashing
- OAuth2 Bearer token authentication

### User Management

- **Trainee:** Students/interns with profiles including university, bio, and skills
- **Company:** Organizations that post internship opportunities

### Core Functionality

- Companies can post internship listings
- Trainees can apply to internships
- Application status tracking (pending, rejected, accepted)
- Skill management with proficiency levels

## API Endpoints

### Auth Routes

| Method | Endpoint                | Description              |
| ------ | ----------------------- | ------------------------ |
| POST   | `/auth/login`           | Login with email/password |
| POST   | `/auth/trainee/signup`  | Register as trainee       |
| POST   | `/auth/signup/company`  | Register as company       |
| GET    | `/auth/get-profile`     | Get current user profile  |

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd task3
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file with:

   ```env
   SECRET_KEY=your-secret-key-here
   ```

5. **Run the application**

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`



## Database Schema

### Entities

- **User:** Base authentication entity with email and password
- **Trainee:** Extended profile for interns (linked to User)
- **Company:** Organization profile (linked to User)
- **Internship:** Job postings by companies
- **Application:** Trainee applications to internships
- **Skill:** Skills with proficiency levels

### Relationships

- User has one Trainee OR one Company (based on role)
- Company has many Internships
- Trainee has many Skills (many-to-many)
- Trainee has many Applications
- Internship has many Applications

## License

This project is for educational purposes.
# FastApi-Project
