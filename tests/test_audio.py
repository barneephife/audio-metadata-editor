import unittest
from src.player.audio import AudioPlayer  # This will be implemented later

class TestAudioPlayer(unittest.TestCase):
    def setUp(self):
        self.player = AudioPlayer()

    def test_load_file(self):
        """Test loading an audio file"""
        # TODO: Implement test
        pass

    def test_play_pause(self):
        """Test play and pause functionality"""
        # TODO: Implement test
        pass

    def test_metadata(self):
        """Test metadata extraction"""
        # TODO: Implement test
        pass

if __name__ == '__main__':
    unittest.main() 