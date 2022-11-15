// eslint-disable-next-line
import React, { useEffect, useState } from 'react';

import './App.css';
import { ParallaxProvider } from 'react-scroll-parallax'
import { ThemeProvider } from './components/context/ThemeContext';

// import Map from './components/Map';
import Info from './components/Info';
import Header from './components/Header';
import CityInfo from './components/CityInfo';
import ShowCity from './components/ShowCity';
import Background from './components/Background';
import CarbonSavings from './components/CarbonSavings';

import CONFIG from './CONFIG.json'

function App() {

  // const [map, setMap] = useState("")
  // const [co2Savings, setCo2Savings] = useState(0)

  const [firstCityData, setFirstCityData] = useState()
  const [secondCityData, setSecondCityData] = useState()

  const RenderMap = () => {
    return (
      <div style={{justifyContent: "center", textAlign: "center"}}>
        <img src="http://127.0.0.1:8000/figures/" alt="Map" style={{left: "50%"}}/>
      </div>
    )
  }


  // After initial page load, add transition to all elements
  // This removes a flash caused by changing themes
  useEffect(() => {
    document.body.style.setProperty('transition', "all 0.3s ease-out");
  }, [])

  useEffect(() => {
    
    if (firstCityData !== undefined && secondCityData !== undefined) {
      let firstCityName = firstCityData.city
      let secondCityName = secondCityData.city

      fetch(CONFIG.backendServer + "/figures/" + {firstCityName} + "/" + {secondCityName})
      .then(RenderMap)
    }

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

            <div>
              <RenderMap />
            </div>
            
            <div>
              <CarbonSavings />
            </div>

            {/* <p style={{textAlign: "center"}}>Using a train could save up to {} tons of CO2!</p> */}

            <Background />

        </div>
      </ThemeProvider>
    </ParallaxProvider>
  );
}

export default App;
