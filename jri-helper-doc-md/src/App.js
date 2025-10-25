import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [markdown, setMarkdown] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleUpload = async () => {
    if (!file) return alert("Please select a file first.");
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      //const response = await fetch("http://127.0.0.1:5000/upload", {
      const response = await fetch("/upload", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setMarkdown(data.markdown || "No markdown returned");
    } catch (error) {
      alert("Error uploading file: " + error.message);
    }
    setLoading(false);
  };

  const handleDownloadMD = () => {
    const blob = new Blob([markdown], { type: "text/markdown" });
    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = url;
    link.download = "content.md";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  };

  return (
    <div className="container py-5" style={{ maxWidth: "800px" }}>
      <h1 className="mb-4 text-center">DOCX to Markdown Converter</h1>

      <div className="mb-3">
        <input
          type="file"
          className="form-control"
          onChange={handleFileChange}
          accept=".docx,.pdf"
        />
      </div>

      <button
        className="btn btn-primary w-100"
        onClick={handleUpload}
        disabled={loading}
      >
        {loading ? "Converting..." : "Upload & Convert"}
      </button>

      <textarea
        readOnly
        value={markdown}
        rows={20}
        className="form-control mt-4"
        style={{ fontFamily: "monospace", whiteSpace: "pre-wrap" }}
      />

      <button className="btn btn-success mt-3" onClick={handleDownloadMD}>
        Export to .md
      </button>
    </div>
  );
}

export default App;
