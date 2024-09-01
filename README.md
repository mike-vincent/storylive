# Media Collection Flask App

This is a Flask application that displays a collection of media items from a YAML file, with search functionality.

## Setup

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`

## Docker

To run with Docker:

1. Build the image: `docker build -t media-collection-app .`
2. Run the container: `docker run -p 5000:5000 media-collection-app`

Access the app at http://localhost:5000

## Customizing Media Data

Edit the `data.yaml` file to add your own media items. Each item should include:

- id: A unique identifier
- title: The title of the media item
- series: The series it belongs to (if applicable)
- type: The type of media (e.g., audio, video)
- genre: The genre of the media
- release_date: The initial release date
- description: A brief description of the media item
- people: An array of people involved (name and role)
- files: An array of file objects, each with a url

## Features

- Displays media items with details and HTML5 players
- Search functionality to filter media items
- Responsive design for various screen sizes