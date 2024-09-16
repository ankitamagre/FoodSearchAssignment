1. Prerequisites
   python (Ensure Python is installed)
   Django (Install using pip install django)
   Django REST Framework (Install using pip install djangorestframework)
   django-filter (Install using pip install django-filter)
   SimpleJWT for authentication (Install using pip install djangorestframework-simplejwt)

2. Project Setup Instructions
  git clone <project-repo-url>
  cd project-directory

3. Configure Database
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'food_list_db',
        'USER': 'root', 
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

4. Run Migrations
  python manage.py makemigrations
  python manage.py migrate

5. Runserver
   python manage.py runserver

6. Api Endpoints
   1. Registration:
      URL: auth/register/
      Method: POST
      Description: Register a new user.
      Request Body:json
      {
        "username": "your_user_name",
        "first_name": "first_name",
        "last_name": "last_name",
        "password": "password123"
      }

   2. Login:
      URL: auth/login/
      Method: POST
      Description: Login and retrieve JWT tokens.
      Request Body:
      json
      Copy code
      {
        "username": "user_name",
        "password": "password123"
      }
7. JWT Authentication:
   Use the access token in headers for authenticated requests:
   Authorization: Bearer <your_access_token>

8. Product Listing with Filters:
   URL: /api/products/
   Method: GET
   Description: Retrieve a list of products with pagination and filters.
   Available Filters:
   min_rating: Filter products with a minimum rating.
   max_rating: Filter products with a maximum rating.
   product_category: Filter by product categories (comma-separated values).
   veg_non_veg: Filter by product type (veg or non-veg).
   toppings: Filter by toppings (comma-separated values).

9. Pagination
    /api/products/?page=2
