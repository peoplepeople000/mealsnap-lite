# MealSnap Lite

MealSnap Lite is a web application that allows users to analyze food images and get nutritional information such as calorie estimates. Simply upload a food photo, and the application will identify the food and provide nutritional details.

## Features

- Image upload and preview
- Food type identification
- Calorie estimation
- Nutritional feedback

## Tech Stack

### Frontend
- React.js
- Modern JavaScript (ES6+)
- CSS for styling

### Backend
- Flask (Python)
- RESTful API architecture
- Image processing capabilities

## Installation and Setup

### Prerequisites
- Node.js (v14+ recommended)
- npm or yarn
- Python 3.7+
- pip

### Frontend Setup
1. Clone the repository
   ```
   git clone https://github.com/yourusername/mealsnap-lite.git
   cd mealsnap-lite/frontend
   ```

2. Install dependencies
   ```
   npm install
   ```

3. Start the development server
   ```
   npm start
   ```
   This will run the app in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

### Backend Setup
1. Navigate to the backend directory
   ```
   cd ../backend
   ```

2. Create and activate a virtual environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install Python dependencies
   ```
   pip install -r requirements.txt
   ```

4. Start the Flask server
   ```
   python app.py
   ```
   The backend server will start at [http://localhost:5001](http://localhost:5001).

## Usage

1. Open the application in your browser at [http://localhost:3000](http://localhost:3000).
2. Click on the file input to select a food image from your device.
3. After selecting an image, a preview will appear.
4. Click the "Analyze Image" button to send the image to the backend for processing.
5. View the analysis results displaying the food type, calorie count, and nutritional feedback.

## API Endpoints

### `POST /analyze`
- **Description**: Analyzes an uploaded food image
- **Request**: Multipart form data with an 'image' field
- **Response**: JSON object containing:
  - `food`: Identified food type
  - `calories`: Estimated calorie count
  - `message`: Nutritional feedback or additional information

## Project Structure

```
mealsnap-lite/
├── frontend/                # React frontend application
│   ├── public/              # Static files
│   └── src/                 # React source code
│       ├── App.js           # Main application component
│       ├── index.js         # Application entry point
│       └── index.css        # Global styles
├── backend/                 # Flask backend server
│   └── app.py               # Flask application
└── README.md                # Project documentation
```

## Building for Production

To build the app for production:

```
cd frontend
npm run build
```

This creates an optimized production build in the `build` folder that can be deployed to a web server.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT](https://choosealicense.com/licenses/mit/)
