# Anonymous Chat Application

A simple anonymous chat application built with Flask. Each user is identified by the name "Anonymous" and assigned a unique color for their username. Messages are stored in a JSON file and displayed in real-time.

## Features

- **Anonymous Usernames:** All users are displayed as "Anonymous."
- **Unique Colors:** Each user gets a unique color for their username.
- **Real-Time Updates:** Messages are fetched and displayed in real-time with polling.
- **Simple JSON Storage:** Messages are stored in a JSON file.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/anonymous-chat-app.git
    cd anonymous-chat-app
    ```

2. **Install Dependencies:**

    Create a `requirements.txt` file with the following content:

    ```
    Flask
    Flask-Session
    ```

    Then install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    ```bash
    python app.py
    ```

    The application will start on `http://127.0.0.1:5000/`.

### Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Type your message in the input field and press "Send" or hit "Enter" to send a message.
3. Messages from each user will appear with their assigned color.

### Directory Structure

- `app.py`: The main Flask application file.
- `messages-info/database.json`: The JSON file where messages are stored.
- `templates/index.html`: The HTML template for the chat interface.
- `requirements.txt`: A file listing the dependencies for the project.

### Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.


### Contact

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/Endoykoo).
