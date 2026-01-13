import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import API_BASE_URL from "../config/api";

function Contact() {
  const navigate = useNavigate();

  useEffect(() => {
    // Fetch website data to update title and favicon
    const fetchWebsiteData = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}/api/homepage/`);
        if (response.data.website) {
          // Update title
          if (response.data.website.name) {
            document.title = `${response.data.website.name} - Contact`;
          }
          
          // Update favicon
          if (response.data.website.favicon) {
            let faviconLink = document.querySelector("link[rel='icon']");
            if (!faviconLink) {
              faviconLink = document.createElement('link');
              faviconLink.rel = 'icon';
              document.head.appendChild(faviconLink);
            }
            faviconLink.href = `${API_BASE_URL}${response.data.website.favicon}`;
            faviconLink.type = 'image/svg+xml';
          }
        }
      } catch (err) {
        console.error('Error fetching website data:', err);
      }
    };

    fetchWebsiteData();
  }, []);

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
  });

  const [submitted, setSubmitted] = useState(false);
  const [submittedData, setSubmittedData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    setError(null); // Clear error when user types
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await axios.post(
        `${API_BASE_URL}/api/contact/`,
        formData,
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );

      if (response.data.success) {
        setSubmittedData(formData);
        setSubmitted(true);
        setFormData({ name: "", email: "", message: "" });
      }
    } catch (err) {
      console.error('Error submitting form:', err);
      setError(
        err.response?.data?.error || 
        'Failed to send message. Please try again later.'
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="contact-container">
      <div className="contact-form">
        {/* Back Button */}
        <button
          type="button"
          className="back-button"
          onClick={() => navigate(-1)}
        >
          ← Back
        </button>

        {!submitted ? (
          <>
            <h2>Contact Us</h2>

            <label>
              Name
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                placeholder="Your Name"
                required
              />
            </label>

            <label>
              Email
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="Your Email"
                required
              />
            </label>

            <label>
              Message
              <textarea
                name="message"
                value={formData.message}
                onChange={handleChange}
                placeholder="Your Message"
                required
              />
            </label>

            {error && (
              <div style={{ 
                backgroundColor: "#fee", 
                color: "#c33", 
                padding: "10px", 
                borderRadius: "5px", 
                marginBottom: "15px",
                fontSize: "14px"
              }}>
                {error}
              </div>
            )}

            <button 
              type="submit" 
              onClick={handleSubmit}
              disabled={loading}
              style={{
                opacity: loading ? 0.6 : 1,
                cursor: loading ? 'not-allowed' : 'pointer'
              }}
            >
              {loading ? 'Sending...' : 'Send Message'}
            </button>
          </>
        ) : (
          <>
            <h2 style={{ textAlign: "center", color: "#28a745", marginBottom: "15px" }}>
              Thank you!
            </h2>
            <p style={{ textAlign: "center", color: "#555", marginBottom: "20px" }}>
              Your message has been sent successfully.
            </p>

            {/* Submitted Data */}
            {submittedData && (
              <div style={{ backgroundColor: "#f9f9f9", padding: "15px", borderRadius: "7px", marginBottom: "20px" }}>
                <p><strong>Name:</strong> {submittedData.name}</p>
                <p><strong>Email:</strong> {submittedData.email}</p>
                <p><strong>Message:</strong> {submittedData.message}</p>
              </div>
            )}

            <div style={{ display: "flex", justifyContent: "space-between" }}>
              <button onClick={() => setSubmitted(false)}>Send Another</button>
            </div>
          </>
        )}
      </div>
    </div>
  );
}

export default Contact;
