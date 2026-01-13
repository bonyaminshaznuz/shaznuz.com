import React, { useEffect, useState } from 'react'
import axios from 'axios';
import API_BASE_URL from '../config/api';

function HomePage() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch data from backend with cache busting
    const fetchData = async () => {
      try {
        // Add timestamp to prevent caching
        const timestamp = new Date().getTime();
        const response = await axios.get(`${API_BASE_URL}/api/homepage/`, {
          params: { _t: timestamp }
        });
        
        // Debug: Log the response data
        console.log('API Response:', response.data);
        console.log('Hero Data:', response.data?.hero);
        
        setData(response.data);
        setLoading(false);
        setError(null);
        
        // Update page title and favicon
        if (response.data.website) {
          // Update title
          if (response.data.website.name) {
            document.title = response.data.website.name;
          }
          
          // Update favicon
          if (response.data.website.favicon) {
            let faviconLink = document.querySelector("link[rel='icon']");
            if (!faviconLink) {
              faviconLink = document.createElement('link');
              faviconLink.rel = 'icon';
              document.head.appendChild(faviconLink);
            }
            faviconLink.href = `${API_BASE_URL}${response.data.website.favicon}?t=${timestamp}`;
            faviconLink.type = 'image/svg+xml';
          }
        }
      } catch (err) {
        console.error('Error fetching data:', err);
        console.error('Error details:', err.response?.data || err.message);
        setError(err.response?.data?.error || err.response?.data?.detail || err.message || 'Failed to load data. Please check if the backend server is running.');
        setLoading(false);
      }
    };

    fetchData();
    
    // Refresh data every 30 seconds to get updates
    const interval = setInterval(fetchData, 30000);
    
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    // Smooth scroll functionality
    const anchors = document.querySelectorAll('a[href^="#"]');
    const handleClick = (e) => {
      e.preventDefault();
      const target = document.querySelector(e.currentTarget.getAttribute("href"));
      if (target) {
        const offset = 120;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: "smooth" });
      }
    };
    anchors.forEach(anchor => anchor.addEventListener("click", handleClick));
    if (window.location.hash) {
      const target = document.querySelector(window.location.hash);
      if (target) {
        const offset = 120;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: "smooth" });
      }
    }

    return () => anchors.forEach(anchor => anchor.removeEventListener("click", handleClick));
  }, []);

  if (loading) {
    return (
      <main>
        <div style={{ padding: '50px', textAlign: 'center' }}>Loading...</div>
      </main>
    );
  }

  if (error) {
    return (
      <main>
        <div style={{ 
          padding: '50px', 
          textAlign: 'center', 
          maxWidth: '600px',
          margin: '50px auto',
          backgroundColor: '#fee',
          border: '2px solid #fcc',
          borderRadius: '10px',
          color: '#c33'
        }}>
          <h2 style={{ marginBottom: '20px', fontSize: '24px' }}>⚠️ Error Loading Data</h2>
          <p style={{ marginBottom: '15px', fontSize: '16px' }}>{error}</p>
          <div style={{ marginTop: '20px', fontSize: '14px', color: '#666' }}>
            <p><strong>Possible solutions:</strong></p>
            <ul style={{ textAlign: 'left', display: 'inline-block', marginTop: '10px' }}>
              <li>Check if backend server is running at: {API_BASE_URL}</li>
              <li>Verify API endpoint: {API_BASE_URL}/api/homepage/</li>
              <li>Check browser console (F12) for more details</li>
              <li>Verify CORS settings in backend</li>
            </ul>
          </div>
          <button 
            onClick={() => window.location.reload()} 
            style={{
              marginTop: '20px',
              padding: '10px 20px',
              backgroundColor: '#3b82f6',
              color: 'white',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer',
              fontSize: '16px'
            }}
          >
            🔄 Retry
          </button>
        </div>
      </main>
    );
  }

  if (!data) {
    return (
      <main>
        <div style={{ padding: '50px', textAlign: 'center' }}>No data available</div>
      </main>
    );
  }

  // Destructure data with safe defaults
  const hero = data?.hero || {};
  const website = data?.website || {};
  const educations = data?.educations || [];
  const skill_categories = data?.skill_categories || [];
  const projects = data?.projects || [];

  // Helper function to get value or fallback (handles empty strings, null, undefined)
  const getValue = (value, fallback) => {
    if (value === null || value === undefined) {
      return fallback;
    }
    if (typeof value === 'string') {
      return value.trim() !== '' ? value : fallback;
    }
    return value || fallback;
  };

  // Debug: Log hero data when it changes
  useEffect(() => {
    console.log('Hero data:', hero);
    console.log('Website data:', website);
    console.log('Full data object:', data);
  }, [data, hero, website]);

  return (
    <main>
      <div id="home" key={hero?.full_name || 'hero-section'}>
        <div className="hero-top">
          <div className="hero-top-left">
            <div className="dev-hero"></div>
            <h3>{getValue(hero?.title, 'Web Developer')}</h3>
          </div>
          <div className="hero-top-right">
            <div className="active-hero"></div>
            <p>{getValue(hero?.availability, 'Available Now')}</p>
          </div>
        </div>
        <div className="hero-main">
          <div className="hero-main-left">
            <h1> I'm {getValue(hero?.full_name, 'Kazi Bony Amin (Shaznuz)')}</h1>
            <p>
              {getValue(hero?.short_intro, 'Web Developer from Dhaka, Bangladesh.')} 
              {hero?.company_name && hero.company_name.trim() !== '' && (
                <span className="highlight"> {hero.company_name}</span>
              )}
              {hero?.short_intro && hero.short_intro.trim() !== '' && !hero.short_intro.includes('.') && '.'}
            </p>
            <div className="button-hero">
              <a href={hero?.hireme_link || "#"} className="btn">Hire Me</a>
              <a href={hero?.download_cv_button || "#"} className="btn btn-alt">Download CV</a>
            </div>
          </div>
          <div className="hero-main-right">
            {website?.profile_picture ? (
              <img 
                src={`${API_BASE_URL}${website.profile_picture}?t=${new Date().getTime()}`} 
                alt="Profile Picture"
                onError={(e) => {
                  e.target.src = './image/pp.jpg';
                }}
              />
            ) : (
              <img src="./image/pp.jpg" alt="Profile Picture" />
            )}
          </div>
        </div>
        <div className="hero-bottom">
          <p>{getValue(hero?.long_biography, 'No biography available.')}</p>
        </div>
      </div>

      <div id="about">
        <div className="education-top">
          <div className="education-top-left">
            <div className="dev-edu"></div>
            <h3>Education & Training</h3>
          </div>
          <div className="education-top-right">
            <a href=""><span>View more</span> <i className="fas fa-arrow-right"></i></a>
          </div>
        </div>
        <div className="education-main">
          {educations && educations.length > 0 ? (
            educations.map((edu, index) => (
              <div key={index} className="education-box">
                <div className="education-main-top-left">
                  <div className="main-edu"></div>
                  <h4>{edu.training_type}</h4>
                </div>
                <div className="edu-box-main">
                  <p className="insti">{edu.institution_name}</p>
                  <p className="subject"><strong>Subject: </strong>{edu.subject}</p>
                  <p className="gpa">
                    <strong>{edu.cgpa ? 'CGPA:' : 'Status:'}</strong> {edu.cgpa || 'Completed'}
                  </p>
                  <p className="pass-year"><strong>Year:</strong> {edu.year}</p>
                </div>
              </div>
            ))
          ) : (
            <div className="education-box">
              <div className="education-main-top-left">
                <div className="main-edu"></div>
                <h4>No Education Data</h4>
              </div>
            </div>
          )}
        </div>
        <div id="myskill">
          <div className="myskill-top">
            <div className="myskill-top-left">
              <div className="dev-edu"></div>
              <h3>My Skills</h3>
            </div>
          </div>
          <div className="bottom-line"></div>
          {skill_categories && skill_categories.length > 0 ? (
            skill_categories.map((category, index) => (
              <div key={index} className="myskill-top">
                <div className="myskill-top-left">
                  <div className="dev-edu"></div>
                  <h4>{category.name}</h4>
                </div>
                <div className="skill-set">
                  {category.skills && category.skills.length > 0 ? (
                    category.skills.map((skill, skillIndex) => (
                      <img 
                        key={skillIndex} 
                        src={skill.icon ? `${API_BASE_URL}${skill.icon}` : `./icon/${skill.name.toLowerCase()}.svg`} 
                        alt={skill.name} 
                      />
                    ))
                  ) : (
                    <p>No skills in this category</p>
                  )}
                </div>
              </div>
            ))
          ) : (
            <div className="myskill-top">
              <div className="myskill-top-left">
                <div className="dev-edu"></div>
                <h4>No Skills Data</h4>
              </div>
            </div>
          )}
        </div>

        <div id="project">
          <div className="myskill-top">
            <div className="project-top-left">
              <div className="dev-edu"></div>
              <h3>My Projects</h3>
            </div>
          </div>
          <div className="project-bottom-line"></div>
          <div className="project-main">
            {projects && projects.length > 0 ? (
              projects.map((project, index) => (
                <div key={index} className="project-card">
                  <div className="project-top">
                    <h3>{project.difficulty_level}</h3>
                  </div>
                  <div className="project-middle">
                    <h3>{project.project_type}</h3>
                    {project.logo ? (
                      <img src={`${API_BASE_URL}${project.logo}`} alt={project.name} />
                    ) : (
                      <img src="./image/qiit.jpg" alt={project.name} />
                    )}
                    <h5>{project.status}</h5>
                  </div>
                  <div className="project-bottom">
                    <a href={project.project_link || "#"}>View</a>
                    <h4>
                      {project.start_date 
                        ? new Date(project.start_date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }).toUpperCase()
                        : 'N/A'
                      }
                    </h4>
                  </div>
                </div>
              ))
            ) : (
              <div className="project-card">
                <div className="project-top">
                  <h3>No Projects</h3>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </main>
  )
}

export default HomePage
