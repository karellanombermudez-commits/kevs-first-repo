const API = "http://localhost:8000";
document.getElementById("go").onclick = async () => {
  const res = await fetch(`${API}/predict`, {
    method: "POST", headers: {"Content-Type": "application/json"},
    body: JSON.stringify([{id: 1, feature_1: 0.3, feature_2: -1.2, category: "a"}]),
  });
  document.getElementById("out").textContent = JSON.stringify(await res.json(), null, 2);
};
