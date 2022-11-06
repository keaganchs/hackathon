import React, { useContext, useState } from 'react';
import { ThemeContext, themes } from './ThemeContext';

import ChangeToDarkIcon from '../../assets/ChangeToDarkIcon.png'
import ChangeToLightIcon from '../../assets/ChangeToLightIcon.png'

function ThemeTogglerButton() {
  const {theme, setTheme} = useContext(ThemeContext)
  const [themeChangeIcon, setThemeChangeIcon] = useState(ChangeToDarkIcon)
  
  const toggleTheme = () => {
    if (theme === themes.dark) {
      setTheme(themes.light)
      setThemeChangeIcon(ChangeToDarkIcon)
    } else {
      setTheme(themes.dark)
      setThemeChangeIcon(ChangeToLightIcon)
    }
  }

  return (
    <button id={"ToggleThemeButton"} onClick={toggleTheme} style={{backgroundColor:theme.headerBackground}}>
      <img src={themeChangeIcon} alt="Small sun or moon icon to switch between the light or dark theme" width={"50px"} height={"50px"}/>
    </button>
  );
}

export default ThemeTogglerButton;