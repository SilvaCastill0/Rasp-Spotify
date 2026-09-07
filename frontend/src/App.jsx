import "./App.css"
import { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://192.168.1.216:5000/now")
        .then(response => response.json())
        .then(data => {
          setData(data);
        });
    }, 1000);

    return () => {
      clearInterval(interval);
    };
  }, []);

  return (
    <>
      {data && (
        <div className="box">
          <div className="table">
            <div className="left">
                <img className="cover-img"
                src = {data.cover.url}
                alt="Album Cover" />
            </div>
            <div className="right">
              <div className="nest">
                <span-track>{data.track}</span-track>
              </div>
              <div>
                <span-artist>{data.artist}</span-artist>
              </div>
            </div>  
          </div>
        </div>
        
      )}
    </>
  );
}

export default App;
