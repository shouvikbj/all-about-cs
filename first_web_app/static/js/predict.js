document.getElementById("predict-btn").addEventListener("click", async () => {
  // const pregnancies = document.getElementById('pregnancies').value;
  // const glucose = document.getElementById('glucose').value;
  // const blood_pressure = document.getElementById('blood_pressure').value;
  // const skin_thickness = document.getElementById('skin_thickness').value;
  // const insulin = document.getElementById('insulin').value;
  // const bmi = document.getElementById('bmi').value;
  // const dpf = document.getElementById('dpf').value;
  // const age = document.getElementById('age').value;

  // Create a data object to send to the server
  // const data = {
  //     pregnancies: pregnancies,
  //     glucose: glucose,
  //     blood_pressure: blood_pressure,
  //     skin_thickness: skin_thickness,
  //     insulin: insulin,
  //     bmi: bmi,
  //     dpf: dpf,
  //     age: age
  // };

  const formData = document.getElementById("diabetes-form");

  // Send the data to the server using fetch
  await fetch("http://localhost:5001/predict/diabetes", {
    method: "POST",
    body: new FormData(formData),
  })
    .then((response) => {
      return response.json();
    })
    .then((result) => {
      const result_view = document.getElementById("result-view");
      result_view.innerText = `Result: ${result.result}`;
      alert(result.result);
    });
});
