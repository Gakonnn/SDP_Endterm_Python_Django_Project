# E-commerce Project in Django

## Introduction

This project is a simplified e-commerce web application built using Django. The primary goal is to demonstrate the use of software design patterns in a real-world scenario while implementing essential e-commerce functionalities. The application allows users to view products, apply discounts and tags dynamically, place orders, and track order statuses.

## Project Goals

1. **Demonstrate Design Patterns**: Implement and showcase creational, structural, and behavioral design patterns.
2. **Build Core E-commerce Features**: Provide functionality for viewing products, applying discounts, and managing orders.
3. **Enhance Code Organization**: Use Django’s Model-Template-View (MTV) architecture to ensure clean separation of concerns.
4. **Practice Real-World Problem Solving**: Apply design patterns effectively to solve common challenges in web development.

## Architecture and Design Patterns

### Architecture

The project uses Django’s Model-Template-View (MTV) pattern, which is an adaptation of the Model-View-Controller (MVC) pattern. This architecture was chosen for the following reasons:
- **Separation of Concerns**: MTV keeps the application modular by separating data handling (Model), business logic (View), and user interface (Template).
- **Built-in Tools**: Django’s MTV pattern provides built-in tools for ORM, templating, and URL routing, simplifying the development process.

### Design Patterns

The following design patterns were used in this project:

1. **Singleton Pattern**
   - **Purpose**: Ensures a single instance of the database connection is used across the application.
   - **Usage**: Django’s ORM inherently uses the Singleton pattern for database connections, optimizing resource management.

2. **Decorator Pattern**
   - **Purpose**: Extends the functionality of the `Product` model by adding dynamic tags (e.g., "Featured" or "Sale") and applying discounts.
   - **Usage**: The `ProductDecorator` class enhances `Product` instances with discounts and tags without modifying the original model, providing flexibility and adherence to the Open/Closed Principle.

3. **Observer Pattern**
   - **Purpose**: Notifies users when there’s an update to their order status (e.g., from "Processing" to "Shipped").
   - **Usage**: Upon changing an order’s status, the application triggers a notification to inform users, allowing real-time updates on order statuses.

## Key Features

1. **Product Management**:
   - View a list of products with details such as price and tags.
   - Add new products directly from the main page.
   - Apply discounts dynamically using the decorator pattern.

2. **Order Management**:
   - View all orders with details such as order ID, user email, and status.
   - Create new orders from the main page.
   - Update order statuses and notify users upon changes.

3. **Notifications**:
   - Use the observer pattern to notify users when their order status changes.

## Project Structure

- **`ecommerce_app/models.py`**: Contains models for `Product` and `Order`.
- **`ecommerce_app/views.py`**: Defines views for displaying and managing products and orders.
- **`ecommerce_app/forms.py`**: Contains forms for creating products and orders.
- **`ecommerce_app/decorators/product_decorator.py`**: Implements the `ProductDecorator` class, which adds tags and discounts to products dynamically.
- **`ecommerce_app/observers/order_observer.py`**: Implements the observer pattern to notify users of order status updates.
- **`templates/main_page.html`**: The main page template that displays products and orders and provides forms to add new ones.

## Limitations and Challenges

1. **Basic UI**: The current interface is minimal and could benefit from enhanced styling for a better user experience.
2. **Simplified Notifications**: Currently, notifications are printed to the console instead of being sent as real emails or SMS.
3. **Data Precision**: Calculations involving discounts require careful handling of `Decimal` values for accurate results.
4. **Limited Order and Product Features**: Advanced features such as cart management, product categories, and user accounts are not yet implemented.

## Future Improvements

1. **UI Enhancements**: Improve the user interface with better styling and layout.
2. **Real Notifications**: Implement email or SMS notifications for user updates.
3. **Additional Design Patterns**: Introduce patterns such as the Factory pattern for handling different product types.
4. **Extended E-commerce Features**:
   - Shopping cart functionality.
   - User authentication for a personalized experience.
   - Payment processing for real-world transactions.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:
   Open your browser and go to `http://127.0.0.1:8000/` to view the main page and manage products and orders.

