import React, { useEffect, useState } from 'react';

export const themes = {
  light: {
    foreground: 'black',
    background: 'white',
    headerBackground: 'white',
    highlight: 'gray',
    text: 'black',
    link: 'darkblue',
    gradientDark: 'rgb(235, 235, 235)',
    gradientLight: 'rgb(253, 253, 253)'
  },
  dark: {
    foreground: 'white',
    background: 'black',
    headerBackground: 'rgb(20, 20, 20)',
    highlight: 'gray',
    text: 'white',
    link: 'lightblue',
    gradientDark: 'rgb(25, 25, 25)',
    gradientLight: 'rgb(20, 20, 20)'
  }
}

export const ThemeContext = React.createContext()

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState(themes.light)
  useEffect(() => {
    document.documentElement.style.setProperty('--main-color', theme.foreground);
    document.documentElement.style.setProperty('--highlight-color', theme.highlight);
    document.documentElement.style.setProperty('--background-color', theme.background);
    document.documentElement.style.setProperty('--header-background', theme.headerBackground);
    document.documentElement.style.setProperty('--header-highlight', theme.highlight);
    document.documentElement.style.setProperty('--main-text-color', theme.text);
    document.documentElement.style.setProperty('--link-text-color', theme.link);
    document.documentElement.style.setProperty('--background-gradient-dark', theme.gradientDark);
    document.documentElement.style.setProperty('--background-gradient-light', theme.gradientLight);

  }, [ theme ])

  return (
    <ThemeContext.Provider value={{theme, setTheme}}>
      {children}
    </ThemeContext.Provider>
  );
}