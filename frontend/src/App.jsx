import { useState } from 'react';
import { Routes, Route, useLocation } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './routes/HomePage';
import Footer from './components/Footer';
import Contact from './routes/Contact';

function App() {
  const [count, setCount] = useState(0);
  const location = useLocation();

  const showLayout = location.pathname === '/'; // only show navbar/footer on MainPage

  return (
    <>
      {showLayout && <Navbar />}
      <Routes>
        <Route path='/' element={<HomePage />} />
        <Route path='/contact' element={<Contact />} />
      </Routes>
      {showLayout && <Footer />}
    </>
  );
}

export default App;
