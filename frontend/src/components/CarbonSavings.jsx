import React from "react";
import { useEffect, useState } from "react";
import '../App.css'
import { useParallax } from 'react-scroll-parallax';

import CONFIG from "../CONFIG.json"

const CarbonSavings = ({distance, population}) => {
  const cityDataURL = CONFIG.backendServer + "/savings/"
  const parallax = useParallax({ speed: -5 });

  const [carbonSavings, setCarbonSavings] = useState(300000)

  // Autocomplete searched city
  // useEffect(() => {
  //   fetch(cityDataURL + "number_of_commuters=" + 30000 + "&distance=" + 2000)
  //   .then(async (response) => {
  //     return await response.json()
  //   })
  //   .then(json => {
  //     setCarbonSavings(json)
  //   })
  // }, [distance, population])

  // Console log suggested city array
  // useEffect(() => {
  //   console.log(suggestedCities)
  // }, [suggestedCities])

  return (
    <div className="CarbonSavingsContainer" ref={parallax.ref}>
      <h2 style={{textAlign: "center"}}>{carbonSavings !== undefined ? carbonSavings : ""}</h2>
    </div>
  )
}

export default CarbonSavings;