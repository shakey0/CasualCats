import React from "react";
import CatList from "./CatList";
import CatProfile from "./CatProfile";

const App = ({ cat }) => {
  return <div>{cat === "home" ? <CatList /> : <CatProfile cat={cat} />}</div>;
};

export default App;
