import React, { useContext } from 'react';
import '../App.css'
import { ThemeContext } from './context/ThemeContext';
import ThemeTogglerButton from './context/ThemeTogglerButton';

// import { useEffect } from 'react';

const Header = () => {

  const {theme} = useContext(ThemeContext)

  return (
    <div className="header" style={{color:theme.foreground, backgroundColor:theme.background}}>
      <h1>Welcome to <i>Carbon Trainer</i></h1>

      <ThemeTogglerButton />
    </div>
  );
}

export default Header;