import React from 'react'
import { NavLink } from 'react-router-dom';

function Navbar() {
    const handleNavClick = (e, targetId) => {
        e.preventDefault();
        const target = document.querySelector(targetId);
        if (target) {
            const offset = 120;
            const top = target.getBoundingClientRect().top + window.scrollY - offset;
            window.scrollTo({ top, behavior: "smooth" });
        }
    };

    return (
        <header>
            <nav>
                <div className="navbar-left">
                    <a href="#home" onClick={(e) => handleNavClick(e, '#home')}>
                        <img src="./icon/home.svg" alt="Home" />
                    </a>
                    <a href="#about" onClick={(e) => handleNavClick(e, '#about')}>
                        <img src="./icon/education.svg" alt="About" />
                    </a>
                    <a href="#myskill" onClick={(e) => handleNavClick(e, '#myskill')}>
                        <img src="./icon/project.svg" alt="Skills" />
                    </a>
                    <a href="#project" onClick={(e) => handleNavClick(e, '#project')}>
                        <img src="./icon/product.svg" alt="Projects" />
                    </a>
                </div>
                <div className="navbar-right">
                    <NavLink to="/contact">
                        <img src="./icon/mail4.svg" alt="Contact Icon" />
                        <span className="hide-on-mobile">Contact Me</span>
                    </NavLink>
                </div>
            </nav>
        </header>
    )
}

export default Navbar