# FitnessTracker
This is my final project for **Django Advanced** - the second module of the course **Python Web** by **Softuni** (Software University)


SoftUni - https://softuni.bg/

Judge system - https://judge.softuni.org/

![image](https://github.com/user-attachments/assets/ead0d208-5b45-4b52-be7c-4fb073000b78)
![image](https://github.com/user-attachments/assets/4a938554-91f2-4212-b0d6-869403a754b9)


## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Models Overview](#models-overview)
- [Admin Panel](#admin-panel)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
Fitness Tracker is a web-based application designed to help users manage their fitness routines, track meals, log workout progress, and explore detailed workout plans. The application is built using Django and adheres to best practices for scalability and maintainability.

---

## Features
- **User Management:**
  - Custom user model (`AppUser`) with email-based authentication.
  - User profiles with additional information such as height, weight, and profile pictures.

- **Workouts Section:**
  - Categorized workout plans with detailed descriptions, benefits, and expectations.
  - User-specific favorite workouts.

- **Meals Section:**
  - Add, edit, and manage meals with calorie tracking.

- **Progress Tracking:**
  - Log exercises with notes and track progress over time.

- **Admin Panel:**
  - Manage users, workouts, meals, and progress logs with custom admin configurations.

---

## Installation

### Prerequisites
- Python 3.8+
- Django 4.x
- PostgreSQL (or another database supported by Django)
- Node.js (for optional front-end build tools)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/username/fitness-tracker.git
    cd fitness-tracker
    ```
2. Set up a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the database:
    - Update `DATABASES` in `settings.py` with your database credentials.
    - Run migrations:
      ```bash
      python manage.py migrate
      ```
5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```

---

## Usage
1. Visit the local server at `http://127.0.0.1:8000`.
2. Register or log in to access features.
3. Use the admin panel (`/admin`) to manage content.

---

## Project Structure

```bash
FitnessTracker/ 
| 
|-- accounts/ # User management app
|-- common/ # Shared utilities and homepage
|-- meals/ # Meals management app
|-- progress/ # Progress tracking app 
|-- workouts/ # Workouts and categories app
|-- templates/ # HTML templates 
|-- media/ # Images
|-- static/ # Static assets (CSS, JS)
|-- manage.py # Django management script 
|-- requirements.txt # Python dependencies
```

---

## Models Overview

### Accounts App
- **AppUser:** Custom user model with fields for email, username, first name, and last name.
- **Profile:** Extends user information with height, weight, and a short description.

### Meals App
- **Meal:** Tracks meals with fields for name, calories, ingredients, and notes.

### Progress App
- **ProgressExercise:** User-specific exercises.
- **ProgressLog:** Logs for exercise performance and tracking over time.

### Workouts App
- **WorkoutCategory:** Categories of workouts with descriptions and images.
- **Workout:** Detailed workout plans with fields for duration, difficulty, calories burned, and more.
- **FavouriteWorkouts:** User-specific favorites list for quick access to workouts.

---

## Admin Panel
The admin panel includes custom configurations for:
- Managing users and profiles.
- CRUD operations for workouts, categories, meals, progress logs, and exercises.
