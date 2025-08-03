// script.js
async function fetchSensorData() {
  try {
    const res = await fetch('/sensor-data');
    const data = await res.json();

    const tbody = document.querySelector("#sensor-table tbody");
    tbody.innerHTML = "";  // Clear table

    data.forEach(entry => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${entry.id}</td>
        <td>${entry.temperature.toFixed(1)}</td>
        <td>${new Date(entry.timestamp).toLocaleString()}</td>
      `;
      tbody.appendChild(row);
    });
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

fetchSensorData();
setInterval(fetchSensorData, 5000);
