import React, { useState } from 'react';

function App() {
  const [image, setImage] = useState(null); // Store the image file
  const [previewURL, setPreviewURL] = useState(null); // Store the URL for image preview
  const [result, setResult] = useState(null); // store analysis result

  const handleImageChange = (e) => {
    const file = e.target.files[0]; // Get the first image selected by the user
    if (!file) return;

    setImage(file); // Save to state
    setPreviewURL(URL.createObjectURL(file)); // Convert to a URL for preview
    setResult(null); // reset result if new image selected
  };

  const handleAnalyze = async () => {
    if (!image) return;

    const formData = new FormData();
    formData.append('image', image);

    try {
      const response = await fetch('http://localhost:5001/analyze', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      setResult(data); // update result to show on UI
    } catch (err) {
      console.error('Error uploading image:', err);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>MealSnap Lite</h1>
      <input type="file" accept="image/*" onChange={handleImageChange} />

      {previewURL && (
        <div style={{ marginTop: 20 }}>
          <p>Image Preview:</p>
          <img src={previewURL} alt="Preview" width="300" />
          <br />
          <button onClick={handleAnalyze} style={{ marginTop: 10 }}>
            Analyze Image
          </button>
        </div>
      )}

      {result && (
        <div style={{ marginTop: 20 }}>
          <h3>Analysis Result:</h3>
          <p><strong>Food:</strong> {result.food}</p>
          <p><strong>Calories:</strong> {result.calories}</p>
          <p><strong>Message:</strong> {result.message}</p>
        </div>
      )}
    </div>
  );
}

export default App;