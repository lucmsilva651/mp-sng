import json
import os
import zipfile

def create_metadata(midi_file):
    metadata = {}
    metadata['name'] = input("Music Name: ")
    metadata['author'] = input("Music Author: ")
    metadata['mapper'] = input("Mapper's Name: ")
    metadata['song_file'] = os.path.basename(midi_file)
    metadata['audio_file'] = metadata['song_file']
    metadata['version'] = 1
    return metadata

def create_zip(midi_file, metadata):
    zip_file = metadata['name'].replace(' ', '_') + '.zip'
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        zipf.write(midi_file, arcname=metadata['song_file'])
        metadata_file = 'metadata.json'
        zipf.writestr(metadata_file, json.dumps(metadata))

def main():
    midi_file = input("Path to MIDI file: ")
    if not os.path.isfile(midi_file):
        print("MIDI file not found.")
        return
    
    metadata = create_metadata(midi_file)
    create_zip(midi_file, metadata)
    print("ZIP file generated successfully!")

if __name__ == "__main__":
    main()
