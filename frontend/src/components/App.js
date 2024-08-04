import React from "react";
import CatList from "./CatList";

const App = ({ cat }) => {
  return (
    <div>
      {cat === "home" ? (
        <CatList />
      ) : (
        <div>
          <h1>It's {cat}!</h1>
        </div>
      )}
    </div>
  );
};

export default App;
