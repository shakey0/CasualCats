import React from "react";
import { createRoot } from "react-dom/client";
import App from "./components/App";

const container = document.getElementById("root");
const root = createRoot(container);
const cat_data = document.getElementById("cat");
if (!cat_data) {
  root.render(<App cat="home" />);
} else {
  const cat = cat_data.dataset.cat;
  root.render(<App cat={cat} />);
}
