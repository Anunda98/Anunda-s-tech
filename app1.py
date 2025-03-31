from flask import Flask, render_template
import requests

app = Flask(__name__)

# Mock data - in a real app, this would come from a database
properties = {
    'bedsitter': [
        {'id': 1, 'title': 'Modern Bedsitter in Utawala', 'price': '15,000', 'location': 'Utawala', 'image': 'bedsitter1.jpg'},
        # Add more bedsitters
    ],
    'onebedroom': [
        {'id': 1, 'title': 'Spacious 1-Bedroom Apartment', 'price': '25,000', 'location': 'Utawala', 'image': 'onebed1.jpg'},
        # Add more one-bedrooms
    ],
    'twobedroom': [
        {'id': 1, 'title': 'Luxury 2-Bedroom Apartment', 'price': '35,000', 'location': 'Utawala', 'image': 'twobed1.jpg'},
        # Add more two-bedrooms
    ],
    'other': [
        {'id': 1, 'title': 'Commercial Space for Rent', 'price': '50,000', 'location': 'Utawala', 'image': 'other1.jpg'},
        # Add more other properties
    ]
}

# Function to fetch social media posts
def get_social_media_posts():
    # This would make API calls to TikTok and Facebook in a real implementation
    # For now, we'll return mock data
    return {
        'tiktok': [
            {'id': '1', 'embed_code': '<blockquote class="tiktok-embed">Mock TikTok 1</blockquote>'},
            {'id': '2', 'embed_code': '<blockquote class="tiktok-embed">Mock TikTok 2</blockquote>'}
        ],
        'facebook': [
            {'id': '1', 'embed_code': '<div class="fb-post">Mock FB Post 1</div>'},
            {'id': '2', 'embed_code': '<div class="fb-post">Mock FB Post 2</div>'}
        ]
    }

@app.route('/')
def home():
    featured = [
        properties['bedsitter'][0],
        properties['onebedroom'][0],
        properties['twobedroom'][0]
    ]
    social_posts = get_social_media_posts()
    return render_template('index.html', featured=featured, social_posts=social_posts)

@app.route('/bedsitter')
def bedsitter():
    return render_template('bedsitter.html', properties=properties['bedsitter'])

@app.route('/onebedroom')
def onebedroom():
    return render_template('onebedroom.html', properties=properties['onebedroom'])

@app.route('/twobedroom')
def twobedroom():
    return render_template('twobedroom.html', properties=properties['twobedroom'])

@app.route('/other')
def other():
    return render_template('other.html', properties=properties['other'])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)