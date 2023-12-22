# Hospital Management System Backend

## Overview
The Hospital Management System (HMS) is a comprehensive backend solution designed to manage various aspects of a hospital's operation. This includes managing doctors, patients, appointments, and more. Built with Django and Django REST Framework, this system ensures a robust, secure, and scalable platform for healthcare facilities.

## Features
- **Doctor Management**: Add, update, and remove doctors along with their specializations.
- **Patient Management**: Keep track of patient information and medical history.
- **Appointment Scheduling**: Schedule and manage appointments between doctors and patients.
- **Secure Authentication**: Manage user access with secure authentication mechanisms.
- **RESTful API**: Easy-to-use API endpoints for integration with various frontend systems.

## Installation

### Prerequisites
- Python 3.8 or above
- pip and virtualenv

### Setting up the project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sohitdeveloper/hospital-management-be.git
   cd hospital-management-be

2. **Setup Virtual Environment**:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**:
    pip install -r requirements.txt

4. **Apply Migrations**:
    python manage.py migrate

5. **Run the Server**:
  python manage.py runserver
