# Image Viewer with Kivy

This is a simple Image Viewer application built using Python and the Kivy framework. The application allows users to input the file name or browse for an image file and display it within the app. It supports multiple image formats like JPG, JPEG, and PNG.

## Features

- **Text Input:** Users can enter the file name of an image manually.
- **File Chooser:** A visual file picker for selecting images from any folder.
- **Error Handling:** Displays an error message if the file is not found or invalid.
- **Multiple Layouts:** Supports flexible UI designs using Kivy layouts.

---

## Requirements

Make sure you have the following installed:

1. **Python** (>= 3.7)
2. **Kivy** (>= 2.1.0)

You can install the necessary libraries by running:
```bash
pip install -r requirements.txt
```

### `requirements.txt`:
```
kivy==2.1.0
```

---

## Installation and Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/image-viewer.git
   ```

2. Navigate to the project folder:
   ```bash
   cd image-viewer
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python find_photo.py
   ```

---

## How to Use

1. Launch the application by running `find_photo.py`.
2. **Option 1:**
   - Type the file name (e.g., `image.jpg`) into the text input field.
   - Press the "Open Image" button to display the image.
3. **Option 2:**
   - Use the file chooser to navigate and select an image.
   - The image will be displayed in the app.
4. If the file is not found or invalid, an error message will be displayed.

---

## File Structure

```
image-viewer/
├── find_photo.py       # Main application file
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
└── images/             # (Optional) Example images
```

---

## Screenshots

1. **Main Screen:**
   - A text input field to enter the file name.
   - A button to open the file.

2. **File Chooser Screen:**
   - A file picker to browse and select images.

3. **Error Screen:**
   - Displays error messages when invalid files are selected.

(Add screenshots here if needed)

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For any questions or suggestions, feel free to reach out:
- Name:Harish Srinivasan [harishoffic@gmail.com]
- GitHub: https://github.com/harishoffic
