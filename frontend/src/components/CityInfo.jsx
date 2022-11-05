import React from "react";
import { useEffect, useState } from "react";
import '../App.css'

import CONFIG from "../CONFIG.json"

const CityInfo = () => {
  const cityDataURL = CONFIG.backendServer + "/cities/"
  
  const [cityData, setCityData] = useState()
  const [cityId, setCityId] = useState()

  const [searchedCity, setSearchedCity] = useState("")
  const [suggestedCities, setSuggestedCities] = useState([])

  // Autocomplete searched city
  useEffect(() => {
    fetch(cityDataURL + "autocomplete?term=" + searchedCity, {method:"POST"})
    .then(async (response) => {
      return await response.json()
    })
    .then(json => {
      setSuggestedCities(json)
    })
  }, [searchedCity])

  // Console log suggested city array
  useEffect(() => {
    console.log(suggestedCities)
  }, [suggestedCities])

  const showCity = ({cityData}) => {
    console.log("cityData: " + cityData)
    
    return (
      <div>
        
      </div>
    )
  } 

  return (
    <div style={{position: "relative"}}>
      <input type="text" name="citySearch" defaultValue={""} onChange={e => setSearchedCity(e.target.value)} />
      <p>
        {suggestedCities?.map((city, i) => {
          return (
            <li key={"city" + i}>
              <button onClick={e => showCity(city)}>{city.city}</button>
            </li>
          );
        })}
      </p>
    </div>
  )
}

export default CityInfo;