# app19_restaurant_menu - Simple Menu/Meals page and minimal admin interface
![DEMO](https://i.imgur.com/IMD8yfK.gif)

This is a Django-based web application for managing a restaurant menu.

## Features

- Display a list of menu items.
- Filter and search for menu items in the admin interface.
- View detailed information about each menu item.

## Models

- `Item`: Represents a menu item. Each item has a meal type, status, and price.

## Views

- `MenuList`: Displays a list of menu items, ordered by the date they were created.
- `MenuItemDetail`: Displays detailed information about a specific menu item.

## URLs

- `home`: The home page, displaying the list of menu items.
- `menu_item`: The detail view for a specific menu item, accessed by its primary key.

## Admin

The Django admin site is used to manage the menu items. The admin interface for `Item` includes a list display, list filter, and search fields.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages using `pip install -r requirements.txt`.
4. Run the server using `python manage.py runserver`.

## Usage

- Visit `localhost:8000` in your web browser to view the menu.
- Visit `localhost:8000/admin` to access the admin site.

