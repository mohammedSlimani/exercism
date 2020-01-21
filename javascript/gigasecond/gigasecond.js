export const gigasecond = (date) => {
  const GIGA1000 = 1000000000000; //gigasecond to milliseconds for a smooth addition
  return new Date(date.getTime() + GIGA1000);
};
