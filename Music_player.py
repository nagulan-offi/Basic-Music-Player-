def create_playlist():

def next_song(song_list, current_song):
    """Selects the next song in the playlist."""
    if current_song < len(song_list) - 1:
        current_song += 1
        play_song(song_list, current_song)
    else:
        print("Reached the end of the playlist.")
    return current_song

def previous_song(song_list, current_song):
    if current_song > 0:
        current_song -= 1
        play_song(song_list, current_song)
    else:
        print("Reached the beginning of the playlist.")
    return current_song

def main():
    song_list = create_playlist()
    current_song = 0
    global is_paused, is_playing  # Declare global flags for play and pause state
    is_paused = False
    is_playing = False

    while True:
        print("\nMusic Player")
        print("1. Play")
        print("2. Pause")
        print("3. Resume")
        print("4. Stop")
        print("5. Next Song")
        print("6. Previous Song")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            play_song(song_list, current_song)
        elif choice == '2':
            pause_song(song_list, current_song)
        elif choice == '3':
            resume_song(song_list, current_song)  
        elif choice == '4':
            stop_song(song_list, current_song)
        elif choice == '5':
            current_song = next_song(song_list, current_song)
        elif choice == '6':
            current_song = previous_song(song_list, current_song)
        elif choice == '7':
            print("Exiting Music Player.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    import time  # Simulate short playback duration
    main()

