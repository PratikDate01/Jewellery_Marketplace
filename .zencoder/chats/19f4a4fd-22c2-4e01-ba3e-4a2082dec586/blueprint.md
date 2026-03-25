# Project Blueprint: Jewellery E-Commerce Marketplace

## 1. Backend Architecture (Django)

### Folder Structure
```
backend/
├── accounts/          # Custom User, Auth, Roles
├── products/          # Products, Categories, Variants
├── orders/            # Order processing, Tracking
├── cart/              # Shopping cart management
├── payments/          # Payment integration
├── reviews/           # Ratings and Reviews
├── suppliers/         # Supplier specific logic
├── wholesale/         # Wholesale pricing and tiers
├── coupons/           # Discount coupons
├── analytics/         # Sales and User analytics
├── config/            # Project settings and URLs
└── manage.py
```

### Key Models
- **User**: `email`, `username`, `role` (choices: ADMIN, CUSTOMER, WHOLESALER, SUPPLIER), `phone`, `address`.
- **Category**: `name`, `slug`, `parent` (for subcategories).
- **Product**: `vendor`, `category`, `name`, `description`, `base_price`, `wholesale_price`, `discount_price`, `stock`, `sku`, `is_featured`, `is_new_arrival`.
- **ProductImage**: `product`, `image`.
- **ProductVariant**: `product`, `size`, `weight`, `purity`.
- **Order**: `user`, `total_amount`, `status`, `shipping_address`, `payment_method`, `payment_status`, `tracking_id`.
- **OrderItem**: `order`, `product`, `quantity`, `price`.
- **Review**: `user`, `product`, `rating` (1-5), `comment`.

### API Endpoints
- `/api/auth/`: `register/`, `login/`, `logout/`, `refresh/`, `profile/`.
- `/api/products/`: List, Create, Retrieve, Update, Delete.
- `/api/categories/`: List categories and subcategories.
- `/api/cart/`: Get, Add, Update, Remove items.
- `/api/orders/`: Place order, List orders, Order details.
- `/api/suppliers/`: Dashboard stats, My products.
- `/api/admin/`: User management, Analytics, Approvals.

## 2. Frontend Architecture (React)

### Folder Structure
```
frontend/
├── src/
│   ├── assets/        # Images, Styles
│   ├── components/    # Reusable components (Navbar, Footer, Sidebar, Cards)
│   ├── layouts/       # Dashboard and Main layouts
│   ├── pages/         # Home, Shop, ProductDetails, Dashboards, Auth
│   ├── redux/         # Store, Slices (auth, product, cart, order)
│   ├── services/      # API calls (Axios instances)
│   ├── utils/         # Helpers, Constants
│   ├── App.js
│   └── main.jsx
├── tailwind.config.js
└── package.json
```

### Redux State Management
- **auth**: `user`, `token`, `isAuthenticated`, `role`.
- **products**: `items`, `loading`, `error`, `selectedProduct`.
- **cart**: `cartItems`, `totalQuantity`, `totalAmount`.
- **orders**: `orderHistory`, `currentOrder`.

### Routing (Protected Routes)
- `/`: Home
- `/shop`: Product Listing
- `/product/:id`: Details
- `/login`, `/register`: Auth
- `/dashboard/customer/*`: Customer Panel
- `/dashboard/wholesaler/*`: Wholesaler Panel
- `/dashboard/supplier/*`: Supplier Panel
- `/dashboard/admin/*`: Admin Panel

## 3. Tech Stack
- **Frontend**: React, Tailwind CSS, Redux Toolkit, Axios, React Router.
- **Backend**: Django, DRF, JWT, MySQL.
- **Theme**: Luxury feel (Gold/Black/White).
