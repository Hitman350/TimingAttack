const socket = io();
let attackChart;
let attackRunning = false;

// Initialize Chart.js
document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById("attackChart").getContext("2d");
    attackChart = new Chart(ctx, {
        type: "line",
        data: {
            labels: [],
            datasets: [{
                label: "Encryption Time (ms)",
                borderColor: "blue",
                backgroundColor: "rgba(0, 0, 255, 0.2)",
                data: [],
                borderWidth: 1,
                pointRadius: 3,
                pointHoverRadius: 5,
                tension: 0.3,
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: "Attempts" } },
                y: { title: { display: true, text: "Time (ms)" }, beginAtZero: true }
            }
        }
    });
});

// Start Attack
function startAttack() {
    if (!attackRunning) {
        attackRunning = true;
        socket.emit("start_stream");
    }
}

// Stop Attack
function stopAttack() {
    if (attackRunning) {
        attackRunning = false;
        socket.emit("stop_stream");
    }
}

// Listen for new data
socket.on("new_data", (data) => {
    if (!attackRunning) return;  // Stop updating chart if attack is stopped

    let lastIndex = attackChart.data.labels.length > 0
        ? attackChart.data.labels[attackChart.data.labels.length - 1]
        : 0;

    if (attackChart.data.labels.length > 50) {
        attackChart.data.labels.shift();
        attackChart.data.datasets[0].data.shift();
    }

    attackChart.data.labels.push(lastIndex + 1);  // Ensure labels increment correctly
    attackChart.data.datasets[0].data.push(data.time);
    attackChart.update();
});
