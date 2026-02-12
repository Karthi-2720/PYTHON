from flask import Flask, send_from_directory, render_template, request, jsonify
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
MUSIC_DIR = r"/storage/emulated/0/music_server/music"
PLAYLISTS_FILE = "playlists.json"
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'flac', 'm4a', 'ogg', 'aac', 'wma'}

# Ensure music directory exists
os.makedirs(MUSIC_DIR, exist_ok=True)

def allowed_file(filename):
    """Check if file has an allowed audio extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_playlists():
    """Load playlists from JSON file"""
    if os.path.exists(PLAYLISTS_FILE):
        with open(PLAYLISTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_playlists(playlists):
    """Save playlists to JSON file"""
    with open(PLAYLISTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(playlists, f, indent=2, ensure_ascii=False)

@app.route("/")
def index():
    songs = os.listdir(MUSIC_DIR)
    songs_json = json.dumps(songs)
    return render_template('index.html', songs=songs, songs_json=songs_json)

@app.route("/music/<path:filename>")
def music(filename):
    return send_from_directory(MUSIC_DIR, filename)

@app.route("/upload", methods=['POST'])
def upload_file():
    """Handle file upload"""
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files provided'}), 400
    
    files = request.files.getlist('files[]')
    uploaded = []
    errors = []
    
    for file in files:
        if file.filename == '':
            continue
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(MUSIC_DIR, filename)
            
            # Handle duplicate filenames
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(filepath):
                filename = f"{base}_{counter}{ext}"
                filepath = os.path.join(MUSIC_DIR, filename)
                counter += 1
            
            file.save(filepath)
            uploaded.append(filename)
        else:
            errors.append(f"{file.filename} - Invalid file type")
    
    return jsonify({
        'success': True,
        'uploaded': uploaded,
        'errors': errors,
        'count': len(uploaded)
    })

@app.route("/playlists", methods=['GET'])
def get_playlists():
    """Get all playlists"""
    playlists = load_playlists()
    return jsonify(playlists)

@app.route("/playlists", methods=['POST'])
def create_playlist():
    """Create a new playlist"""
    data = request.get_json()
    playlist_name = data.get('name', '').strip()
    
    if not playlist_name:
        return jsonify({'error': 'Playlist name is required'}), 400
    
    playlists = load_playlists()
    
    if playlist_name in playlists:
        return jsonify({'error': 'Playlist already exists'}), 400
    
    playlists[playlist_name] = []
    save_playlists(playlists)
    
    return jsonify({'success': True, 'name': playlist_name})

@app.route("/playlists/<playlist_name>", methods=['DELETE'])
def delete_playlist(playlist_name):
    """Delete a playlist"""
    playlists = load_playlists()
    
    if playlist_name not in playlists:
        return jsonify({'error': 'Playlist not found'}), 404
    
    del playlists[playlist_name]
    save_playlists(playlists)
    
    return jsonify({'success': True})

@app.route("/playlists/<playlist_name>/songs", methods=['GET'])
def get_playlist_songs(playlist_name):
    """Get songs in a playlist"""
    playlists = load_playlists()
    
    if playlist_name not in playlists:
        return jsonify({'error': 'Playlist not found'}), 404
    
    return jsonify({'songs': playlists[playlist_name]})

@app.route("/playlists/<playlist_name>/add", methods=['POST'])
def add_to_playlist(playlist_name):
    """Add a song to a playlist"""
    data = request.get_json()
    song = data.get('song', '').strip()
    
    if not song:
        return jsonify({'error': 'Song name is required'}), 400
    
    playlists = load_playlists()
    
    if playlist_name not in playlists:
        return jsonify({'error': 'Playlist not found'}), 404
    
    if song not in playlists[playlist_name]:
        playlists[playlist_name].append(song)
        save_playlists(playlists)
    
    return jsonify({'success': True})

@app.route("/playlists/<playlist_name>/remove", methods=['POST'])
def remove_from_playlist(playlist_name):
    """Remove a song from a playlist"""
    data = request.get_json()
    song = data.get('song', '').strip()
    
    if not song:
        return jsonify({'error': 'Song name is required'}), 400
    
    playlists = load_playlists()
    
    if playlist_name not in playlists:
        return jsonify({'error': 'Playlist not found'}), 404
    
    if song in playlists[playlist_name]:
        playlists[playlist_name].remove(song)
        save_playlists(playlists)
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)