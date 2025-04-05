# AP Biology Study Notes

A web application for AP Biology study notes based on the College Board curriculum.

## Features

- Organized by AP Biology units (1-8)
- Responsive design for all devices
- Easy navigation between units and topics
- Clean and modern user interface

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://localhost:5000`

## Project Structure

- `app.py`: Main Flask application
- `templates/`: HTML templates
- `static/`: CSS and other static files
- `requirements.txt`: Python dependencies

## Adding Content

To add new study notes, you'll need to add them to the database. You can do this through the Flask shell:

```bash
flask shell
```

Then create new topics:

```python
from app import db, Topic
new_topic = Topic(title="Your Topic Title", content="Your content here", unit=1)
db.session.add(new_topic)
db.session.commit()
```

## License

MIT License 