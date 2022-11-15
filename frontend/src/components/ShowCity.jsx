import React from "react"

import { useParallax } from 'react-scroll-parallax';

// Required parameters: cityData: pydantic_models.city
const ShowCity = ({cityData}) => {  
  const parallax = useParallax({ speed: -5 });

  return (
    cityData !== undefined ? (
    <div className="CityDataContainer" ref={parallax.ref}>
      <h3>{cityData.city}, {cityData.country}</h3>
      <p>Population: <i>{new Intl.NumberFormat('en-US', { maximumSignificantDigits: 4 }).format(cityData.population)}</i></p>
    </div>
    ) : <div className="CityDataContainer" ref={parallax.ref}></div>
  )
} 

export default ShowCity