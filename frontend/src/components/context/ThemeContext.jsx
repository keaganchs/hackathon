import React, { useEffect, useState } from 'react';

export const themes = {
  light: {
    foreground: 'black',
    background: 'white',
    highlight: 'gray',
    text: 'black',
    link: 'darkblue'
  },
  dark: {
    foreground: 'white',
    background: 'black',
    highlight: 'gray',
    text: 'white',
    link: 'lightblue'
  }
}

export const ThemeContext = React.createContext()

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState(themes.light)
  useEffect(() => {
    document.documentElement.style.setProperty('--main-color', theme.foreground);
    document.documentElement.style.setProperty('--highlight-color', theme.highlight);
    document.documentElement.style.setProperty('--background-color', theme.background);
    document.documentElement.style.setProperty('--header-background', theme.background);
    document.documentElement.style.setProperty('--header-highlight', theme.highlight);
    document.documentElement.style.setProperty('--main-text-color', theme.text);
    document.documentElement.style.setProperty('--link-text-color', theme.link);

  }, [ theme ])

  return (
    <ThemeContext.Provider value={{theme, setTheme}}>
      {children}
    </ThemeContext.Provider>
  );
}