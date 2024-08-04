import React from "react";

const CatList = () => {
  const [cats, setCats] = React.useState([]);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    fetch("/api/cats")
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        return res.json();
      })
      .then((data) => {
        setCats(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Fetch error:", error);
        setLoading(false);
      });
  }, []);

  return (
    <div>
      <h1>Cats</h1>
      {loading && <p>Loading...</p>}
      {!loading && cats.length > 0 && (
        <div>
          {cats.map((cat, index) => (
            <div key={index}>{cat}</div>
          ))}
        </div>
      )}
    </div>
  );
};

export default CatList;
