import React from "react"

// Required parameters: cityData: pydantic_models.city
const ShowCity = ({cityData}) => {  
  return (
    cityData !== undefined ? (
    <div className="CityDataContainer">
      <h3>{cityData.city}, {cityData.country}</h3>
      <p>Population: <i>{new Intl.NumberFormat('en-US', { maximumSignificantDigits: 4 }).format(cityData.population)}</i></p>
    </div>
    ) : <div className="CityDataContainer"></div>
  )
} 

export default ShowCity