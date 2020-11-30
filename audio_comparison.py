from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
import json


with open("dejavu.cnf.SQLITE_SAMPLE") as f:
    config = json.load(f)
djv = Dejavu(config)

songs = []
def audio_compare(indexed_audio):
	print indexed_audio
	for audio_file in indexed_audio:
		print audio_file
		songs.append(djv.recognize(FileRecognizer,audio_file))
	return songs
def audio_fingerprint(directory):
	djv.fingerprint_directory(str(directory) + "/audio_output/", [".mp3"])
