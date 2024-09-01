from flask import Flask, render_template, request
import yaml

app = Flask(__name__)

def load_data():
    with open('data.yaml', 'r') as file:
        return yaml.safe_load(file)

def search_media(query, media_items):
    query = query.lower()
    return [item for item in media_items if 
            query in item['title'].lower() or
            query in item['description'].lower() or
            query in item['series'].lower() or
            query in item['genre'].lower() or
            any(query in person['name'].lower() or query in person['role'].lower() 
                for person in item['people'])]

@app.route('/')
def index():
    data = load_data()
    search_query = request.args.get('search', '').strip()
    if search_query:
        media_items = search_media(search_query, data['media_items'])
    else:
        media_items = data['media_items']
    return render_template('index.html', media_items=media_items, search_query=search_query)

if __name__ == '__main__':
    app.run(debug=True)