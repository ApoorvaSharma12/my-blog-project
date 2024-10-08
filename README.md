`# My Blog Project

## _A Simple Django Blog Application_

![Blog Logo](https://cldup.com/dTxpPi9lDf.thumb.png) <!-- You can replace this with an actual image link if available -->

This project is a simple blog application built using Django. It allows users to create, read, update, and delete blog posts, as well as add comments to each post. The application features tagging functionality, a user authentication system, and a comment liking feature.

## Features

- User authentication (sign up and login)
- Create, edit, and delete blog posts
- Tagging functionality for blog posts
- Comment on blog posts
- Like comments
- Share blog posts via email

## Prerequisites

To run this project, you need to have the following installed:

- **Python 3.x**: Download from [python.org](https://www.python.org/downloads/).
- **PostgreSQL**: Download and install from [postgresql.org](https://www.postgresql.org/download/).

## Installation Steps

Follow these steps to set up the project locally:

1. **Clone the repository**:
   Open your terminal (command prompt) and run the following command:
   ```bash
   git clone https://github.com/ApoorvaSharma12/my-blog-project.git
   cd my-blog-project `

1.  **Create a virtual environment** (optional but recommended): This keeps your project dependencies isolated.

    bash

    Copy code

    `python -m venv venv`

2.  **Activate the virtual environment**:

    -   On **Windows**:

        bash

        Copy code

        `venv\Scripts\activate`

    -   On **macOS/Linux**:

        bash

        Copy code

        `source venv/bin/activate`


3.  **Set up the PostgreSQL database**:

    -   Open PostgreSQL and create a new database for the project (e.g., `my_blog_db`).
    -   You can use pgAdmin or the command line to create the database.
4.  **Configure the database settings**: Open `settings.py` in your Django project and update the `DATABASES` settings with your database credentials. For example:

    python

    Copy code

    `DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'my_blog_db',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }`

5.  **Apply migrations**: Run the following command to create the necessary database tables:

    bash

    Copy code

    `python manage.py migrate`

6.  **Create a superuser** (to access the Django admin):

    bash

    Copy code

    `python manage.py createsuperuser`

    Follow the prompts to create your superuser account.

7.  **Run the development server**: Start the server with the following command:

    bash

    Copy code

    `python manage.py runserver`

8.  **Access the application**: Open your web browser and navigate to `http://127.0.0.1:8000/`.

Usage
-----

-   **Sign Up**: Create a new user account using the sign-up page.
-   **Login**: Access your account using your credentials.
-   **Create Blog Posts**: Use the Django admin interface to create and manage blog posts.
-   **Commenting**: Users can leave comments on blog posts.
-   **Like Comments**: Users can like comments made on blog posts.
-   **Tagging**: Add tags to your blog posts to categorize them.

![image](https://github.com/user-attachments/assets/bd8a4b78-0ccb-470e-ad19-2527a642873d)
![image](https://github.com/user-attachments/assets/745b5d9e-5942-419c-a06b-18a30ded8456)
![image](https://github.com/user-attachments/assets/781bd95b-3660-4bd4-adff-6039b62791bc)

