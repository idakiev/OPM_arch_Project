# OPM /arch

This project is a comprehensive organizer designed for architectural companies to efficiently manage their projects, clients, and team members. It provides features for project tracking, resource management, client engagement, and user authentication.

---
### Short Preview

https://github.com/idakiev/OPM_arch_Project/assets/122561971/b75eb2f8-9d1e-4073-907c-059f1a96ca58

---

## Table of Content

- [Usage](https://github.com/idakiev/OPM_arch_Project#usage)
- [Features](https://github.com/idakiev/OPM_arch_Project#features)
- [Technologies Used](https://github.com/idakiev/OPM_arch_Project#Technologies%20Used)
- [Installation](https://github.com/idakiev/OPM_arch_Project#installation)
- [License](https://github.com/idakiev/OPM_arch_Project#license)

## Usage

This project management organizer allows architectural companies to perform the following tasks:

 - Project Management: Store detailed information about projects, assign team members, track progress, and set deadlines.

 - Client Engagement: Clients can create accounts, monitor project progress, upload resources, and communicate with the team through the messaging feature.

 - User Authentication: Users (employees and clients) are authenticated using a secure login system with temporary passwords upon signup.

 - Role-Based Permissions: Different user roles (e.g., team leaders, project managers) have varying levels of access and permissions within the system.

## Features
- User Authentication: New users receive temporary passwords and must change them upon initial login. Users can manage their profiles and upload profile pictures.

- Role-Based Access Control: Administrators, project managers, and team leaders have different permissions for managing clients, projects, and employee information.

 - Project Details: Each project can be associated with key information such as project type, phase, project manager, assigned team members, progress, and deadlines.

## Technologies Used

<p align="left">
  <a href="#"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a>
  <a href="#"><img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/></a>
  <a href="#"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/></a>
  <a href="#"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/></a>
</p>

## Installation

1. Clone the repository:
    ```
      https://github.com/idakiev/OPM_arch_Project.git
    ```
3. Install dependencies:
    ```
      pip install -r requirements.txt
    ```
4. Set up the environment variables:
  - Create a .env file in the root directory and add the necessary variables (see envExample.txt file).
4. Apply migrations:
    ```
      python manage.py migrate
    ```
5. Create superuser:
    ```
      python manage.py createsuperuser
    ```
6. Start development server:
   ```
     python manage.py runserver
   ```
7. Access the application in your web browser at http://127.0.0.1:8000.

## License
This section is licensed under the [MIT License](LICENSE).
