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

  return (
    <div>
      <button onClick={handlePlay}>
        Play
      </button>

      <button onClick={handlePause}>
	Pause
      </button>
    </div>
  );
}

export default App;
