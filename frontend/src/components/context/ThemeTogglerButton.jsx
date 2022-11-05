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
    <button id={"ToggleThemeButton"} onClick={toggleTheme} style={{backgroundColor:theme.background, color:theme.foreground}}>
      <img src={themeChangeIcon} alt="Sun and moon icon to toggle light and dark themes" width={"50px"} height={"50px"}/>
    </button>
  );
}

export default ThemeTogglerButton;