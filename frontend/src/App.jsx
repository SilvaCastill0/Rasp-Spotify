import "./App.css"

function App() {
   async function handlePlay() {
    const response = await fetch("http://127.0.0.1:5000/resume");
    const text = await response.text();

    console.log(text);
  }

  async function handlePause() {
    const response = await fetch("http://127.0.0.1:5000/pause");
    const text = await response.text();

    console.log(text);
  }

  async function handleNext() {
    const response = await fetch("http://127.0.0.1:5000/next");
    const text = await response.text();

    console.log(text);
  }

  async function handlePrev() {
    const response = await fetch("http://127.0.0.1:5000/prev");
    const text = await response.text();

    console.log(text);
  }

  async function handlevolume() {
    const response = await fetch("http://127.0.0.1:5000/volume");
    const text = await response.text();

    console.log(text);
  }

  async function handleSeek() {
    const response = await fetch("http://127.0.0.1:5000/seek");
    const text = await response.text();

    console.log(text);
  }

  




  return (
    <div>
      <button className="play-button" onClick={handlePlay}>
        Play
      </button>

      <button onClick={handlePause}>
	      Pause
      </button>

      <button onClick={handleNext}>
	      Next
      </button>

      <button onClick={handlePrev}>
	      Prev
      </button>

      <button onClick={handlevolume}>
	      Volume
      </button>

      <button onClick={handleSeek}>
	      Seek
      </button>
    </div>
  );
}

export default App;
