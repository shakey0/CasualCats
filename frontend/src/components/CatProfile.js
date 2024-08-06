import React from "react";

const CatProfile = ({ cat }) => {
  const [profile, setProfile] = React.useState({});
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    fetch(`/api/${cat}`)
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        return res.json();
      })
      .then((data) => {
        setProfile(data);
        console.log(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Fetch error:", error);
        setLoading(false);
      });
  }, [cat]);

  return (
    <div>
      <h1>{cat}</h1>
      <p>{profile.cat}</p>
      HERERERERE
      {!loading && Object.keys(profile).length > 0 && (
        <div>
          <p>{profile.desc}</p>
          {profile.photos &&
            profile.photos.map((photo, index) => (
              <img
                key={index}
                src={`data:image/jpeg;base64,${photo}`}
                alt={`cat-${index}`}
              />
            ))}
        </div>
      )}
    </div>
  );
};

export default CatProfile;
