import React, { useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom';
import axios from 'axios';
import API_BASE_URL from '../config/api';

function Footer() {
    const [footerData, setFooterData] = useState(null);
    const [socialIcons, setSocialIcons] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchFooterData = async () => {
            try {
                const response = await axios.get(`${API_BASE_URL}/api/homepage/`);
                if (response.data) {
                    setFooterData(response.data.footer);
                    setSocialIcons(response.data.social_icons || []);
                }
                setLoading(false);
            } catch (err) {
                console.error('Error fetching footer data:', err);
                setLoading(false);
            }
        };

        fetchFooterData();
    }, []);

    if (loading) {
        return (
            <footer>
                <div className="footer-bottom">
                    <p>Loading...</p>
                </div>
            </footer>
        );
    }

    return (
        <footer>
            <div className="footer-top">
                <h1>{footerData?.title || "Let's work together."}</h1>
                <p>{footerData?.small_talk || "Creating user experience and visual appealing design"}</p>
                <div className="footer-contact">
                    <a href={footerData?.hire_me_link || "#"}>Hire Me</a>
                    <NavLink to="/contact">Contact Me</NavLink>
                </div>
            </div>

            <div className="footer-middle">
                <div className="footer-middle-left">
                    <div className="footer-dot"></div>
                    <p>Follow Me</p>
                </div>
                <div className="footer-middle-right">
                    {socialIcons && socialIcons.length > 0 ? (
                        socialIcons.map((icon, index) => (
                            <a 
                                key={index} 
                                href={icon.icon_link} 
                                target="_blank" 
                                rel="noopener noreferrer"
                            >
                                {icon.icon ? (
                                    <img 
                                        src={`${API_BASE_URL}${icon.icon}`} 
                                        alt={`Social Icon ${index + 1}`} 
                                    />
                                ) : (
                                    <span>Icon</span>
                                )}
                            </a>
                        ))
                    ) : (
                        // Fallback to default social icons if no data
                        <>
                            <a href="https://github.com/bonyaminshaznuz" target="_blank" rel="noopener noreferrer">
                                <img src="./icon/github-svgrepo-com.svg" alt="GitHub" />
                            </a>
                            <a href="https://bd.linkedin.com/in/bonyaminshaznuz" target="_blank" rel="noopener noreferrer">
                                <img src="./icon/linkedin-svgrepo-com.svg" alt="LinkedIn" />
                            </a>
                            <a href="https://www.facebook.com/bonyshaznuz/" target="_blank" rel="noopener noreferrer">
                                <img src="./icon/facebook-svgrepo-com.svg" alt="Facebook" />
                            </a>
                            <a href="https://www.instagram.com/bonyaminshaznuz/" target="_blank" rel="noopener noreferrer">
                                <img src="./icon/instagram-svgrepo-com.svg" alt="Instagram" />
                            </a>
                        </>
                    )}
                </div>
            </div>

            <div className="footer-bottom">
                <p>{footerData?.copyright_text || "Copyright © Shaznuz"}</p>
            </div>
        </footer>
    )
}

export default Footer