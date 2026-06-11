

---

# Simple E-Commerce Store

A full-stack e-commerce web application built using Django. The platform allows users to browse products, view product details, manage a shopping cart, place orders, and manage their accounts.

---

## Features

### User Authentication

* User Registration
* User Login
* User Logout
* Secure Authentication System

### Product Management

* View Product Listings
* Product Detail Page
* Product Categories
* Product Images
* Product Pricing Information

### Shopping Cart

* Add Products to Cart
* Remove Products from Cart
* Update Product Quantity
* Cart Total Calculation

### Order Processing

* Place Orders
* Order Summary
* Order History


### Admin Panel

* Manage Products
* Manage Orders
* Manage Users
* Manage Categories

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates

### Backend

* Python
* Django

### Database

* SQLite (Development)
---

## Project Structure

```text
simple_ecommerce/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── store/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── orders/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│
├── static/
│   ├── css/
│   ├── js/
│
├── media/
│
├── manage.py
└── requirements.txt
```

## Installation

### Clone Repository

```bash
git clone https://github.com/Rasaghnya/simple-ecommerce.git

cd simple-ecommerce
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Future Improvements

* Product Search
* Wishlist Feature
* Product Reviews and Ratings
* Online Payment Gateway Integration
* Coupon System
* Email Notifications
* Order Tracking
* REST API using Django REST Framework
* Responsive Mobile Design
* Product Recommendations

---

## Learning Outcomes

This project demonstrates:

* Django Project Structure
* Django Authentication System
* CRUD Operations
* Database Relationships
* Template Rendering
* Form Handling
* Session Management
* Shopping Cart Logic
* Order Processing Workflow
* Full Stack Web Development Concepts

---

## Author

Developed as a learning project to understand full-stack web development using Django, HTML, CSS, JavaScript, and relational databases.

---

### License

This project is open-source and available for educational and learning purposes.
