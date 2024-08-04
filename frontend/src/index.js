import React from "react";
import { createRoot } from "react-dom/client";
import App from "./components/App";

const container = document.getElementById("root");
const cat = document.getElementById("cat").dataset.cat;
console.log(cat);
const root = createRoot(container);
root.render(<App cat={cat} />);
