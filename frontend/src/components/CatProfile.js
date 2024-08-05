import React from "react";

const CatProfile = ({ cat }) => {
  // const [profile, setProfile] = React.useState({});
  // const [loading, setLoading] = React.useState(true);

  // React.useEffect(() => {
  //   fetch(`/api/cats/${cat}`)
  //     .then((res) => {
  //       if (!res.ok) {
  //         throw new Error("Network response was not ok");
  //       }
  //       return res.json();
  //     })
  //     .then((data) => {
  //       setProfile(data);
  //       setLoading(false);
  //     })
  //     .catch((error) => {
  //       console.error("Fetch error:", error);
  //       setLoading(false);
  //     });
  // }, [cat]);

  return (
    <div>
      <h1>{cat}</h1>
      {/* {loading && <p>Loading...</p>}
      {!loading && Object.keys(profile).length > 0 && (
        <div>
          <p>{profile.description}</p>
          <img src={profile.image} alt={cat} />
        </div>
      )} */}
    </div>
  );
};

export default CatProfile;
