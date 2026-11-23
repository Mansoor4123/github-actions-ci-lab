const sampleTestResults = {
  total: 12,
  passed: 12,
  failed: 0,
};

const sampleHistory = [
  { title: "Run #48", detail: "main · latest commit", status: "success", time: "12 min ago" },
  { title: "Run #47", detail: "main · dependency update", status: "success", time: "1 hr ago" },
  { title: "Run #46", detail: "feature/validation · pull request", status: "failure", time: "3 hrs ago" },
];

const passPercent =
  (sampleTestResults.passed / sampleTestResults.total) * 100;

document.querySelector("#total-tests").textContent = sampleTestResults.total;
document.querySelector("#passed-tests").textContent = sampleTestResults.passed;
document.querySelector("#failed-tests").textContent = sampleTestResults.failed;
document.querySelector("#progress-pass").style.width = `${passPercent}%`;

function renderHistory() {
  const historyList = document.querySelector("#history-list");
  historyList.replaceChildren();

  sampleHistory.forEach((run) => {
    const row = document.createElement("div");
    row.className = "history-row";

    const marker = document.createElement("span");
    marker.className = `history-status ${run.status}`;

    const description = document.createElement("div");
    const title = document.createElement("strong");
    title.textContent = run.title;
    const detail = document.createElement("span");
    detail.textContent = run.detail;
    description.append(title, detail);

    const time = document.createElement("span");
    time.textContent = run.time;

    row.append(marker, description, time);
    historyList.append(row);
  });
}

renderHistory();

document.querySelector("#refresh-button").addEventListener("click", () => {
  renderHistory();
});
