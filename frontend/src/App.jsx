// eslint-disable-next-line
import React, { useEffect, useState } from 'react';

import './App.css';
import { ParallaxProvider } from 'react-scroll-parallax'
import { ThemeProvider } from './components/context/ThemeContext';

import Info from './components/Info';
import Header from './components/Header';
import CityInfo from './components/CityInfo';
import ShowCity from "./components/ShowCity";
import Background from './components/Background';

function App() {

  const [firstCityData, setFirstCityData] = useState()
  const [secondCityData, setSecondCityData] = useState()

  // After initial page load, add transition to all elements
  // This removes a flash caused by changing themes
  useEffect(() => {
    document.body.style.setProperty('transition', "all 0.3s ease-out");
  }, [])

  useEffect(() => {
    console.log("First city data: " + firstCityData)
    console.log("Second city data: " + secondCityData)
  }, [firstCityData, secondCityData])

  return (
    <ParallaxProvider>
      <ThemeProvider>
        <div className="App">
            <div className="BackgroundGradient"/>
            <Header />
            <div style={{height:"20vh"}}></div>

            <Info />          

            <div style={{display:"flex", flexDirection:"row", justifyContent: "space-evenly"}}>
              <CityInfo title={"First City"} setCityDataFunc={setFirstCityData}/>
              <CityInfo title={"Second City"} setCityDataFunc={setSecondCityData}/>
            </div>
            
            <div style={{display:"flex", flexDirection:"row", justifyContent: "space-evenly"}}>
              <ShowCity cityData={firstCityData} style={{minWidth: "250px"}}/>
              <ShowCity cityData={secondCityData} style={{minWidth: "250px"}}/>
            </div>

            
            <Background />

        </div>
      </ThemeProvider>
    </ParallaxProvider>
  );
}

export default App;
