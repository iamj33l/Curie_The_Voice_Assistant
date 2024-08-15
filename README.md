# Curie Voice Assistant

Curie is a voice assistant application built using Python. It leverages speech recognition and text-to-speech technologies to interact with users and perform various tasks such as searching Google, playing songs on YouTube, opening applications, and more.

## Features

- **Voice Recognition**: Recognizes user commands through the microphone.
- **Text-to-Speech**: Responds to user commands with synthesized speech.
- **Google Search**: Searches Google for user queries.
- **Play Songs**: Plays songs on YouTube.
- **Open Applications**: Opens specified applications on the user's computer.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/iamj33l/curie-voice-assistant.git
    cd curie-voice-assistant
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv .venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        .\.venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source .venv/bin/activate
        ```

4. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Interact with Curie**:
    - Click the "Speak" button to activate the voice assistant.
    - Speak your command into the microphone.
    - Curie will respond and perform the requested task.

## Project Structure

- `main.py`: The main entry point of the application. Initializes the GUI and handles user interactions.
- `curie.py`: Contains the `Curie` class which processes user commands and executes corresponding tasks.
- `tasks/`: Directory containing task-specific modules such as `play_song.py`, `search_google.py`, and `open_app.py`.
- `requirements.txt`: Lists the dependencies required for the project.

## Dependencies

- `tkinter`: For creating the GUI.
- `speech_recognition`: For recognizing speech from the microphone.
- `pywhatkit`: For performing tasks like playing YouTube videos and searching Google.
- `AppOpener`: For opening applications on the user's computer.
- `pyaudio`: For accessing the microphone.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

###### Made with ❤️ by [Jeel Patel](https://github.com/iamj33l)
