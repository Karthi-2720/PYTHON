let currentPlaylist = 'all';
let currentSongPlaying = null;
let currentSongIndex = -1;
let allSongs = [];
let playlists = {};
let isShuffleOn = false;
let repeatMode = 'off'; // 'off', 'all', 'one'
let currentSongList = [];

// Load data on page load
window.addEventListener('DOMContentLoaded', async () => {
    // Get songs from template
    const songsData = document.querySelector('body').dataset.songs;
    if (songsData) {
        allSongs = JSON.parse(songsData);
    }

    await loadPlaylists();
    setupEventListeners();
    updateCurrentSongList();
    renderSongCards();
});

function setupEventListeners() {
    const player = document.getElementById("player");
    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');

    // Player events
    player.addEventListener('play', () => {
        updatePlayButtonIcon(true);
    });

    player.addEventListener('pause', () => {
        updatePlayButtonIcon(false);
    });

    // Update progress bar
    player.addEventListener('timeupdate', () => {
        if (player.duration) {
            const progress = (player.currentTime / player.duration) * 100;
            document.getElementById('progressFillBottom').style.width = progress + '%';
            document.getElementById('currentTimeBottom').textContent = formatTime(player.currentTime);
        }
    });

    // Update duration when loaded
    player.addEventListener('loadedmetadata', () => {
        document.getElementById('durationBottom').textContent = formatTime(player.duration);
    });

    // Auto-play next song when current ends
    player.addEventListener('ended', () => {
        if (repeatMode === 'one') {
            player.currentTime = 0;
            player.play();
        } else {
            playNext();
        }
    });

    // Drag and drop events
    if (uploadZone) {
        uploadZone.addEventListener('click', () => fileInput.click());

        uploadZone.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadZone.classList.add('drag-over');
        });

        uploadZone.addEventListener('dragleave', () => {
            uploadZone.classList.remove('drag-over');
        });

        uploadZone.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadZone.classList.remove('drag-over');
            const files = e.dataTransfer.files;
            handleFileUpload(files);
        });

        fileInput.addEventListener('change', (e) => {
            handleFileUpload(e.target.files);
        });
    }
}

function updatePlayButtonIcon(isPlaying) {
    const btn = document.getElementById('playBtnLarge');
    if (isPlaying) {
        // Pause Icon
        btn.innerHTML = `
            <svg role="img" height="16" width="16" viewBox="0 0 16 16" fill="currentColor">
                <path d="M2.7 1a.7.7 0 0 0-.7.7v12.6a.7.7 0 0 0 .7.7h2.6a.7.7 0 0 0 .7-.7V1.7a.7.7 0 0 0-.7-.7H2.7zm8 0a.7.7 0 0 0-.7.7v12.6a.7.7 0 0 0 .7.7h2.6a.7.7 0 0 0 .7-.7V1.7a.7.7 0 0 0-.7-.7h-2.6z"></path>
            </svg>
        `;
    } else {
        // Play Icon
        btn.innerHTML = `
            <svg role="img" height="16" width="16" viewBox="0 0 16 16" fill="currentColor">
                <path d="M3 1.713a.7.7 0 0 1 1.05-.607l10.89 6.288a.7.7 0 0 1 0 1.212L4.05 14.894A.7.7 0 0 1 3 14.288V1.713z"></path>
            </svg>
        `;
    }
}

function formatTime(seconds) {
    if (isNaN(seconds)) return '0:00';
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs.toString().padStart(2, '0')}`;
}

function getRandomColor() {
    const colors = [
        'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
        'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
        'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
        'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
        'linear-gradient(135deg, #30cfd0 0%, #330867 100%)',
        'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)',
        'linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)'
    ];
    return colors[Math.floor(Math.random() * colors.length)];
}

function renderSongCards() {
    const recentContainer = document.getElementById('recentSongs');
    const allSongsContainer = document.getElementById('allSongsGrid');

    const playIconSvg = `
        <svg role="img" height="24" width="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M7.05 3.606l13.49 7.788a.7.7 0 0 1 0 1.212L7.05 20.394A.7.7 0 0 1 6 19.788V4.212a.7.7 0 0 1 1.05-.606z"></path>
        </svg>
    `;

    // Show recent 6 songs
    const recentSongs = currentSongList.slice(0, 6);
    recentContainer.innerHTML = recentSongs.map((song, index) => `
        <div class="song-card" onclick="playSongByIndex(${index})">
            <div class="card-image" style="background: ${getRandomColor()}">
                <div class="play-overlay">
                    <button class="play-overlay-btn">${playIconSvg}</button>
                </div>
            </div>
            <div class="card-content">
                <div class="card-title">${song}</div>
                <div class="card-subtitle">Song</div>
            </div>
        </div>
    `).join('');

    // Show all songs
    allSongsContainer.innerHTML = currentSongList.map((song, index) => `
        <div class="song-card" onclick="playSongByIndex(${index})">
            <div class="card-image" style="background: ${getRandomColor()}">
                <div class="play-overlay">
                    <button class="play-overlay-btn">${playIconSvg}</button>
                </div>
            </div>
            <div class="card-content">
                <div class="card-title">${song}</div>
                <div class="card-subtitle">Song</div>
            </div>
        </div>
    `).join('');
}

function updateCurrentSongList() {
    currentSongList = currentPlaylist === 'all' ? [...allSongs] : [...(playlists[currentPlaylist] || [])];
    if (isShuffleOn) {
        shuffleArray(currentSongList);
    }
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function togglePlay() {
    const player = document.getElementById('player');
    if (!currentSongPlaying) {
        // Play first song if none selected
        if (currentSongList.length > 0) {
            playSongByIndex(0);
        }
        return;
    }

    if (player.paused) {
        player.play();
    } else {
        player.pause();
    }
}

function playPrevious() {
    if (currentSongList.length === 0) return;

    currentSongIndex = currentSongIndex - 1;
    if (currentSongIndex < 0) {
        currentSongIndex = repeatMode === 'all' ? currentSongList.length - 1 : 0;
    }
    playSongByIndex(currentSongIndex);
}

function playNext() {
    if (currentSongList.length === 0) return;

    currentSongIndex = currentSongIndex + 1;
    if (currentSongIndex >= currentSongList.length) {
        if (repeatMode === 'all') {
            currentSongIndex = 0;
        } else {
            currentSongIndex = currentSongList.length - 1;
            return; // Don't play if not repeating
        }
    }
    playSongByIndex(currentSongIndex);
}

function playSongByIndex(index) {
    if (index < 0 || index >= currentSongList.length) return;

    currentSongIndex = index;
    const song = currentSongList[index];
    const player = document.getElementById('player');

    player.src = "/music/" + encodeURIComponent(song);
    document.getElementById('playerSongTitle').textContent = song;
    document.getElementById('playerArtist').textContent = 'Unknown Artist';
    currentSongPlaying = song;
    player.play();

    // Show add to playlist button
    document.getElementById('addToPlaylistBtn').style.display = 'block';
}

function toggleShuffle() {
    isShuffleOn = !isShuffleOn;
    const btn = document.getElementById('shuffleBtnSmall');
    btn.classList.toggle('active', isShuffleOn);

    if (isShuffleOn) {
        btn.style.color = 'var(--spotify-green)';
    } else {
        btn.style.color = '';
    }

    updateCurrentSongList();
    renderSongCards();

    // Find current song in new shuffled list
    if (currentSongPlaying) {
        currentSongIndex = currentSongList.indexOf(currentSongPlaying);
    }
}

function toggleRepeat() {
    const modes = ['off', 'all', 'one'];
    const currentIndex = modes.indexOf(repeatMode);
    repeatMode = modes[(currentIndex + 1) % modes.length];

    const btn = document.getElementById('repeatBtnSmall');
    btn.classList.remove('active', 'repeat-one');

    if (repeatMode === 'all') {
        btn.classList.add('active');
        btn.style.color = 'var(--spotify-green)';
    } else if (repeatMode === 'one') {
        btn.classList.add('active', 'repeat-one');
        btn.style.color = 'var(--spotify-green)';
    } else {
        btn.style.color = '';
    }
}

function seekTo(event) {
    const player = document.getElementById('player');
    const progressBar = document.getElementById('progressBarBottom');
    const rect = progressBar.getBoundingClientRect();
    const percent = (event.clientX - rect.left) / rect.width;
    player.currentTime = percent * player.duration;
}

function setVolume(value) {
    const player = document.getElementById('player');
    player.volume = value / 100;
    updateVolumeIcon(value);
}

function toggleMute() {
    const player = document.getElementById('player');
    const slider = document.getElementById('volumeSliderSmall');

    if (player.volume > 0) {
        player.dataset.previousVolume = player.volume;
        player.volume = 0;
        slider.value = 0;
    } else {
        const prevVolume = parseFloat(player.dataset.previousVolume) || 1;
        player.volume = prevVolume;
        slider.value = prevVolume * 100;
    }
    updateVolumeIcon(slider.value);
}

function updateVolumeIcon(value) {
    const btn = document.getElementById('volumeBtnSmall');
    let iconPath = '';

    if (value == 0) {
        // Mute
        iconPath = '<path d="M13.86 5.47a.75.75 0 0 0-1.061 0l-1.47 1.47-1.47-1.47A.75.75 0 0 0 8.8 6.53L10.269 8l-1.47 1.47a.75.75 0 1 0 1.06 1.06l1.47-1.47 1.47 1.47a.75.75 0 0 0 1.06-1.06L12.39 8l1.47-1.47a.75.75 0 0 0 0-1.06z"></path><path d="M10.116 1.5A.75.75 0 0 0 8.991.85l-6.925 4.612H.25a.75.75 0 0 0-.75.75v5.5c0 .414.336.75.75.75h1.816l6.925 4.615a.75.75 0 0 0 1.125-.625V1.5z"></path>';
    } else if (value < 50) {
        // Low volume
        iconPath = '<path d="M9.741.534a.75.75 0 0 1 .259.616v13.7c0 .267-.142.511-.371.636a.75.75 0 0 1-.774-.037l-4.72-3.45H1.25A1.25 1.25 0 0 1 0 10.75v-5.5C0 4.56.56 4 1.25 4h2.885l4.72-3.45a.75.75 0 0 1 .886-.016zM6 10.817V5.183L2.672 7.616a.75.75 0 0 1-.441.144H1.5v3.98h.731c.162 0 .315.053.441.144L6 10.817z"></path>';
    } else {
        // High volume
        iconPath = '<path d="M9.741.534a.75.75 0 0 1 .259.616v13.7c0 .267-.142.511-.371.636a.75.75 0 0 1-.774-.037l-4.72-3.45H1.25A1.25 1.25 0 0 1 0 10.75v-5.5C0 4.56.56 4 1.25 4h2.885l4.72-3.45a.75.75 0 0 1 .886-.016zM6 10.817V5.183L2.672 7.616a.75.75 0 0 1-.441.144H1.5v3.98h.731c.162 0 .315.053.441.144L6 10.817zM12.28 2.22a.75.75 0 0 1 1.06 0c2.292 2.291 2.292 6.009 0 8.3a.75.75 0 0 1-1.06-1.06c1.706-1.706 1.706-4.474 0-6.18a.75.75 0 0 1 0-1.06z"></path><path d="M10.68 4.34a.75.75 0 0 1 1.06 0c1.03 1.03 1.03 2.7 0 3.73a.75.75 0 1 1-1.06-1.06c.445-.445.445-1.166 0-1.61a.75.75 0 0 1 0-1.06z"></path>';
    }

    btn.innerHTML = `
        <svg role="img" height="16" width="16" viewBox="0 0 16 16" fill="currentColor">
            ${iconPath}
        </svg>
    `;
}

async function handleFileUpload(files) {
    if (files.length === 0) return;

    const formData = new FormData();
    for (let file of files) {
        formData.append('files[]', file);
    }

    const progressDiv = document.getElementById('uploadProgress');
    progressDiv.innerHTML = '<div class="progress-item">Uploading files...</div>';
    progressDiv.classList.remove('hidden');

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.success) {
            progressDiv.innerHTML = `
                <div class="progress-item success">
                    ✅ Successfully uploaded ${result.count} file(s)
                </div>
            `;

            // Refresh song list
            setTimeout(() => {
                location.reload();
            }, 1500);
        } else {
            progressDiv.innerHTML = '<div class="progress-item error">❌ Upload failed</div>';
        }
    } catch (error) {
        progressDiv.innerHTML = '<div class="progress-item error">❌ Upload error</div>';
    }

    document.getElementById('fileInput').value = '';
}

async function loadPlaylists() {
    try {
        const response = await fetch('/playlists');
        playlists = await response.json();
        renderPlaylists();
    } catch (error) {
        console.error('Error loading playlists:', error);
    }
}

function renderPlaylists() {
    const container = document.getElementById('playlistItemsSidebar');
    container.innerHTML = '';

    for (let [name, songs] of Object.entries(playlists)) {
        const item = document.createElement('div');
        item.className = 'playlist-item-sidebar';
        item.dataset.playlist = name;
        item.innerHTML = `
            <span onclick="selectPlaylist('${name}')">${name}</span>
            <div class="playlist-actions-sidebar">
                <span class="song-count-sidebar">${songs.length}</span>
                <button class="delete-playlist-btn-sidebar" onclick="deletePlaylist('${name}')" title="Delete">🗑️</button>
            </div>
        `;
        container.appendChild(item);
    }
}

function selectPlaylist(playlistName) {
    currentPlaylist = playlistName;

    // Update active state
    document.querySelectorAll('.playlist-item-sidebar').forEach(item => {
        item.classList.remove('active');
    });
    document.querySelector(`[data-playlist="${playlistName}"]`).classList.add('active');

    // Update current song list for navigation
    updateCurrentSongList();
    renderSongCards();

    // Update current song index if song is playing
    if (currentSongPlaying) {
        currentSongIndex = currentSongList.indexOf(currentSongPlaying);
    }
}

function showCreatePlaylistModal() {
    document.getElementById('createPlaylistModal').classList.remove('hidden');
    document.getElementById('playlistNameInput').focus();
}

function hideCreatePlaylistModal() {
    document.getElementById('createPlaylistModal').classList.add('hidden');
    document.getElementById('playlistNameInput').value = '';
}

async function createPlaylist() {
    const name = document.getElementById('playlistNameInput').value.trim();

    if (!name) {
        alert('Please enter a playlist name');
        return;
    }

    try {
        const response = await fetch('/playlists', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name })
        });

        const result = await response.json();

        if (result.success) {
            await loadPlaylists();
            hideCreatePlaylistModal();
        } else {
            alert(result.error || 'Failed to create playlist');
        }
    } catch (error) {
        alert('Error creating playlist');
    }
}

async function deletePlaylist(name) {
    if (!confirm(`Delete playlist "${name}"?`)) return;

    try {
        const response = await fetch(`/playlists/${encodeURIComponent(name)}`, {
            method: 'DELETE'
        });

        const result = await response.json();

        if (result.success) {
            if (currentPlaylist === name) {
                selectPlaylist('all');
            }
            await loadPlaylists();
        }
    } catch (error) {
        alert('Error deleting playlist');
    }
}

function showAddToPlaylistModal() {
    if (!currentSongPlaying) return;

    const modal = document.getElementById('addToPlaylistModal');
    const listContainer = document.getElementById('playlistSelectList');

    listContainer.innerHTML = '';

    if (Object.keys(playlists).length === 0) {
        listContainer.innerHTML = '<p class="no-playlists">No playlists yet. Create one first!</p>';
    } else {
        for (let name of Object.keys(playlists)) {
            const item = document.createElement('div');
            item.className = 'playlist-select-item';
            item.innerHTML = `
                <span>🎵 ${name}</span>
                <button class="add-btn" onclick="addToPlaylist('${name}')">Add</button>
            `;
            listContainer.appendChild(item);
        }
    }

    modal.classList.remove('hidden');
}

function hideAddToPlaylistModal() {
    document.getElementById('addToPlaylistModal').classList.add('hidden');
}

async function addToPlaylist(playlistName) {
    if (!currentSongPlaying) return;

    try {
        const response = await fetch(`/playlists/${encodeURIComponent(playlistName)}/add`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ song: currentSongPlaying })
        });

        const result = await response.json();

        if (result.success) {
            await loadPlaylists();

            // Show feedback
            const btn = event.target;
            btn.textContent = '✓ Added';
            btn.disabled = true;
            setTimeout(() => {
                btn.textContent = 'Add';
                btn.disabled = false;
            }, 2000);
        }
    } catch (error) {
        alert('Error adding to playlist');
    }
}

function showSettingsModal() {
    document.getElementById('settingsModal').classList.remove('hidden');
}

function hideSettingsModal() {
    document.getElementById('settingsModal').classList.add('hidden');
}

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT') return;

    const player = document.getElementById('player');

    // Spacebar: Play/Pause
    if (e.code === 'Space' && currentSongPlaying) {
        e.preventDefault();
        togglePlay();
    }

    // Arrow Left: Previous track
    if (e.code === 'ArrowLeft') {
        e.preventDefault();
        playPrevious();
    }

    // Arrow Right: Next track
    if (e.code === 'ArrowRight') {
        e.preventDefault();
        playNext();
    }

    // Arrow Up: Volume up
    if (e.code === 'ArrowUp') {
        e.preventDefault();
        const slider = document.getElementById('volumeSliderSmall');
        const newVolume = Math.min(100, parseInt(slider.value) + 10);
        slider.value = newVolume;
        setVolume(newVolume);
    }

    // Arrow Down: Volume down
    if (e.code === 'ArrowDown') {
        e.preventDefault();
        const slider = document.getElementById('volumeSliderSmall');
        const newVolume = Math.max(0, parseInt(slider.value) - 10);
        slider.value = newVolume;
        setVolume(newVolume);
    }

    // M: Mute/Unmute
    if (e.code === 'KeyM') {
        e.preventDefault();
        toggleMute();
    }
});
