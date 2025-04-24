# Blog Platform

A dynamic blogging platform built with Django where users can share their stories and engage with other writers. This platform provides a modern, responsive interface for creating and managing blog content with rich text formatting and image support.

## Core Features

### Current Implementation
- 👤 **User System**
  - Login/Logout functionality
  - Profile management
  - Authentication middleware
  - Secure password handling
  
- 📝 **Blog Management**
  - Create, Edit, and Delete posts
  - Rich text formatting
  - Image uploads and management
  - Post preview functionality
  
- 🎨 **Frontend**
  - Responsive design
  - Bootstrap 5 integration
  - Mobile-friendly interface
  - Clean and intuitive user experience

### Upcoming Features
- 🔐 User registration with email verification
- 📝 Markdown support & rich text editor
- 📁 Categories and tags
- 🔍 Advanced search functionality
- 📱 Progressive Web App (PWA) support

## Technical Stack

### Backend
- Python 3.8+
- Django 4.x
- Django REST Framework
- Django Crispy Forms
- Pillow (for image handling)

### Frontend
- Bootstrap 5
- JavaScript
- HTMX
- Font Awesome icons

## Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL database
- Virtual environment (recommended)

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/blog.git
cd blog
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure the database
- Create a PostgreSQL database
- Update the database settings in `settings.py` with your credentials

5. Run migrations
```bash
python manage.py migrate
```

6. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

7. Collect static files
```bash
python manage.py collectstatic
```

## Running the Project

1. Start the development server
```bash
python manage.py runserver
```

2. Access the application
- Open your browser and navigate to `http://127.0.0.1:8000/`
- Admin interface: `http://127.0.0.1:8000/admin/`

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
- Follow PEP 8 guidelines
- Use Django's coding style for templates and views

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.