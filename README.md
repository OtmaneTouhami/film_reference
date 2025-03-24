# Film Reference Application

A Django web application for managing a collection of films with details like title, director, year, genre, and poster images.

## Project Overview

Film Reference is a web-based application that allows users to:
- Browse a collection of films
- View detailed information about each film
- Add new films to the database
- Edit existing film entries
- Delete films from the collection

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9+ 
- pip (Python package manager)
- MySQL Server 8.0+
- Git

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/otmanetouhami/film_reference.git
cd film_reference
```

2. **Create and activate a virtual environment**

```bash
# For Windows
python -m venv .venv
.venv\Scripts\activate

# For macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

3. **Install required dependencies**

```bash
pip install -r requirements.txt
```

## Database Setup

1. **Create a MySQL database**

```sql
CREATE DATABASE film_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. **Update database configuration**

Create an .env file in the project root and add the following:

```
DB_USERNAME=YOUR_DB_USERNAME
DB_PASSWORD=YOUR_DB_PASSWORD
```

3. **Apply migrations**

```bash
python manage.py migrate
```

4. **Create a superuser for admin access**

```bash
python manage.py createsuperuser
```

## Running the Application

1. **Start the development server**

```bash
python manage.py runserver
```

2. **Access the application**

- Main site: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin/

## Project Structure

- film - Main application with models, views, and templates
- film_reference - Project settings and configuration
- posters - Storage for uploaded film posters
- `static-files/` - Compiled static files (generated when deployed)

## Features

- **Film Management**: Create, read, update, and delete film entries
- **Image Upload**: Upload and display film posters
- **Categorization**: Organize films by genre, year, and director
- **Admin Interface**: Powerful Django admin for database management
- **Responsive Design**: Mobile-friendly interface using TailwindCSS

## Troubleshooting

### Database Connection Issues

If you encounter MySQL connection problems, ensure:
- MySQL server is running
- Credentials in settings.py are correct
- The database exists and is accessible

### Image Upload Problems

If image uploads fail:
- Check that the media directory exists and is writable
- Verify that Pillow is installed correctly
- Make sure the server has sufficient permissions