// eslint-disable-next-line
import React, { useEffect, useState } from 'react';

import './App.css';
import { ParallaxProvider } from 'react-scroll-parallax'
import { ThemeProvider } from './components/context/ThemeContext';

import Header from './components/Header';
import CityInfo from './components/CityInfo';
import Background from './components/Background';


function App() {

  // After initial page load, add transition to all elements
  // This removes a flash caused by changing themes
  useEffect(() => {
    document.body.style.setProperty('transition', "all 0.5s ease-out");
  }, [])

  return (
    <ParallaxProvider>
      <ThemeProvider>
        <div className="App">
            <Header />
            <div style={{height:"20vh"}}></div>

            <CityInfo />
            
            <Background />

            <p>
              Welcome to Carbon Trainer
            </p>

            <p>
              <i>Training Future Generations.</i>
            </p>

        </div>
      </ThemeProvider>
    </ParallaxProvider>
  );
}

export default App;
