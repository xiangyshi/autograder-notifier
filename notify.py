from plyer import notification
import simpleaudio as sa  # Install using: pip install playsound

# File path to a loud alarm sound (replace with your actual file)
ALARM_FILE = "alarm.wav"  # Use any audio file you have


def make_notification():
    print("sending notification...")
    # Custom message
    title = "New Ticket in Queue"
    message = "Go to Autograder ASAP!"

    # Trigger the notification
    notification.notify(
        title=title,
        message=message,
        app_name="Alert",
        timeout=30
    )

    # Play the sound
    try:
        wave_obj = sa.WaveObject.from_wave_file(ALARM_FILE)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until the sound finishes playing
    except Exception as e:
        print(f"Error playing sound: {e}")