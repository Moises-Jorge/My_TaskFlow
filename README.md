# TaskFlow - To-Do List with Django & Bootstrap

**TaskFlow** is an interactive and secure **To-Do List** web application designed to help users organize their daily routines efficiently. The project was developed using the **Django (Python)** framework for the back-end, and **Django Templates combined with Bootstrap** for a modern and responsive user interface.

The main objective of this project was to apply web development best practices, the **MVT (Model-View-Template)** architectural pattern, Django's native authentication system, and efficient data handling through the Django ORM.

---

## 🚀 Features

### 🔐 Authentication and Security
* **Restricted Area:** Secure sign-up, login, and logout system using Django's native authentication system.
* **Data Privacy:** Each authenticated user has exclusive access to their own tasks.

### 📋 Task Management (CRUD)
* **Quick Creation:** Add tasks by specifying a title and an optional description.
* **Reading and Organization:** Clear visualization of pending and completed tasks.
* **Dynamic Update:** Mark tasks as completed or edit their information with a single click.
* **Secure Deletion:** Easily remove tasks from the list.

### 🎨 Interface and User Experience
* **Status Filters:** Quickly filter your tasks between "All", "Pending", and "Completed".
* **Responsive Design:** Interface optimized for desktops, tablets, and mobile devices using Bootstrap.
* **Admin Panel:** Access to **Django Admin** for full control and management of users and tasks in the back-end.

---

## 🛠️ Technologies Used

* **Back-end:** Python 3 and Django Web Framework
* **Front-end:** Django Templates, HTML5, CSS3, and Bootstrap 5
* **Database:** SQLite (Django's default for development)

---

## 📦 How to Run the Project Locally

Follow the steps below to clone the repository and run the application on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/Moises-Jorge/My_TaskFlow.git
cd My_TaskFlow
```

### 2. Create and Activate the Virtual Environment (Virtualenv)
On Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (To access Django Admin)
```bash
python manage.py createsuperuser
```
*(Follow the terminal prompts to set a username, email, and password)*

### 6. Start the Development Server
```bash
python manage.py runserver
```

Now, open your browser and go to:
* **Application:** `http://127.0.0.1:8000/`
* **Admin Panel:** `http://127.0.0.1:8000/admin/`

---

## ⚙️ Data Model Structure (ORM)

The main model of the application was structured as follows:

* `user`: Foreign key (ForeignKey) linked to Django's native user model (`User`).
* `title`: CharField (Task title).
* `description`: TextField (Detailed description, optional).
* `complete`: BooleanField (Task completion status).
* `created_at`: DateTimeField (Automatic creation date and time).

---


