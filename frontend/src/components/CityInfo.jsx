import React from "react";
import { useEffect, useState } from "react";
import '../App.css'
import { useParallax } from 'react-scroll-parallax';

import CONFIG from "../CONFIG.json"

const CityInfo = ({title, setCityDataFunc}) => {
  const cityDataURL = CONFIG.backendServer + "/cities/"
  const parallax = useParallax({ speed: -5 });

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
  }, [searchedCity, cityDataURL])

  // Console log suggested city array
  // useEffect(() => {
  //   console.log(suggestedCities)
  // }, [suggestedCities])

  return (
    <div className="CitySearchContainer" ref={parallax.ref}>
      <h2 style={{textAlign: "center"}}>{title}</h2>
      <input type="text" name="citySearch" defaultValue={""} onChange={e => setSearchedCity(e.target.value)} style={{minWidth: "250px"}} />
      <p>
        {suggestedCities?.map((city, i) => {
          return (
            <li key={"city" + i}>
              <button onClick={e => setCityDataFunc(city)}>{city.city}</button>
            </li>
          );
        })}
      </p>
    </div>
  )
}

export default CityInfo;