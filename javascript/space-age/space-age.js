export const age = (planet,time_seconds) => {
  const PLANETS = {
    "earth":1,
    "mercury":0.2408467,
    "venus":0.61519726,
    "mars":1.8808158,
    "jupiter":11.862615,
    "saturn":29.447498,
    "uranus":84.016846,
    "neptune":164.79132
  };

  const earth_year_seconds = 31557600;
  //the + sign is for convertion to Number
  return +(time_seconds/earth_year_seconds/PLANETS[planet]).toFixed(2);

};
