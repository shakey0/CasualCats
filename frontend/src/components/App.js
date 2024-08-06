import React from "react";
import CatList from "./CatList";
import CatProfile from "./CatProfile";

const App = ({ cat }) => {
  return <>{cat === "home" ? <CatList /> : <CatProfile cat={cat} />}</>;
};

export default App;
