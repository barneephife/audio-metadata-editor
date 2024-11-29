class MetadataPanel(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(380)
        self.setStyleSheet("""
            QFrame {
                background-color: #2a2a2a;
                border: none;
            }
            QLabel {
                color: #cccccc;
                font-size: 11px;
                padding-right: 4px;
            }
        """)
        
        # Initialize all attributes first
        # Editable fields
        self.title = None
        self.artist = None
        self.album_artist = None
        self.album = None
        self.disc_number = None
        self.track = None
        self.year = None
        self.genre = None
        self.comment = None
        self.composer = None
        
        # Read-only labels
        self.filename = QLabel()
        self.path = QLabel()
        self.tag = QLabel()
        self.codec = QLabel()
        self.bitrate = QLabel()
        self.samplerate = QLabel()
        self.length = QLabel()
        self.mode = QLabel()
        self.size = QLabel()
        self.modified = QLabel()
        
        # Cover art widget
        self.cover_art = None
        
        # Apply button
        self.apply_btn = None
        
        # Now set up the UI
        self.setup_ui()