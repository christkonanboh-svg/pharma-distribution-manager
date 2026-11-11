(function () {
  const chartDataElement = document.getElementById("dashboard-chart-data");
  const chartData = chartDataElement ? JSON.parse(chartDataElement.textContent) : {};

  const compactNumber = (value) =>
    Number(value).toLocaleString("fr-FR", {
      minimumFractionDigits: 1,
      maximumFractionDigits: 1,
    });

  const escapeHtml = (value) =>
    String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");

  window.showToast = function (message, type = "success") {
    const root = document.getElementById("toast-root");
    if (!root) return;

    const tones = {
      success: {
        icon: "i-check-circle",
        wrapper: "bg-emerald-50 text-emerald-600",
        border: "border-emerald-100",
      },
      error: {
        icon: "i-alert",
        wrapper: "bg-rose-50 text-rose-600",
        border: "border-rose-100",
      },
      info: {
        icon: "i-sparkles",
        wrapper: "bg-sky-50 text-sky-600",
        border: "border-sky-100",
      },
    };
    const tone = tones[type] || tones.success;

    const toast = document.createElement("div");
    toast.className =
      "toast translate-y-3 opacity-0 transition duration-300 ease-out " +
      tone.border;
    toast.innerHTML = `
      <span class="grid h-9 w-9 shrink-0 place-items-center rounded-xl ${tone.wrapper}">
        <svg class="icon-sm"><use href="#${tone.icon}"></use></svg>
      </span>
      <div class="min-w-0 flex-1">
        <p class="text-xs font-bold text-slate-900">DPCI</p>
        <p class="mt-0.5 text-xs leading-5 text-slate-600">${escapeHtml(message)}</p>
      </div>
      <button type="button" data-toast-close class="grid h-7 w-7 shrink-0 place-items-center rounded-lg text-slate-400 transition hover:bg-slate-100 hover:text-slate-700" aria-label="Fermer">
        <svg class="icon-sm h-3.5 w-3.5"><use href="#i-x"></use></svg>
      </button>
    `;

    root.appendChild(toast);

    requestAnimationFrame(() => {
      toast.classList.remove("translate-y-3", "opacity-0");
    });

    let removed = false;
    const remove = () => {
      if (removed) return;
      removed = true;
      toast.classList.add("translate-y-3", "opacity-0");
      window.setTimeout(() => toast.remove(), 300);
    };

    const timer = window.setTimeout(remove, 4600);
    toast.querySelector("[data-toast-close]").addEventListener("click", () => {
      window.clearTimeout(timer);
      remove();
    });
  };

  document.addEventListener("alpine:init", () => {
    Alpine.data("dashboard", () => ({
      period: "7j",
      chart: null,
      revenueTotal: "",

      init() {
        this.updateTotal();
        this.$nextTick(() => this.renderChart());
      },

      updateTotal() {
        const series = chartData[this.period] || { revenue: [] };
        const total = series.revenue.reduce((sum, value) => sum + value, 0);
        this.revenueTotal = compactNumber(total) + " M";
      },

      setPeriod(period) {
        if (this.period === period) return;
        this.period = period;
        this.updateTotal();
        this.renderChart();
      },

      renderChart() {
        const canvas = this.$refs.revenueChart;
        const series = chartData[this.period];
        if (!canvas || !series || typeof Chart === "undefined") return;

        if (this.chart) {
          this.chart.destroy();
        }

        const context = canvas.getContext("2d");
        const gradient = context.createLinearGradient(0, 0, 0, 300);
        gradient.addColorStop(0, "rgba(16, 172, 148, 0.28)");
        gradient.addColorStop(0.55, "rgba(16, 172, 148, 0.08)");
        gradient.addColorStop(1, "rgba(16, 172, 148, 0)");

        Chart.defaults.font.family = '"Plus Jakarta Sans", sans-serif';
        Chart.defaults.color = "#94a3b8";

        this.chart = new Chart(context, {
          type: "line",
          data: {
            labels: series.labels,
            datasets: [
              {
                label: "Ventes",
                data: series.revenue,
                borderColor: "#0b8a79",
                backgroundColor: gradient,
                fill: true,
                tension: 0.42,
                borderWidth: 2.5,
                pointRadius: 0,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "#ffffff",
                pointHoverBorderColor: "#0b8a79",
                pointHoverBorderWidth: 2,
              },
              {
                label: "Commandes",
                data: series.orders,
                borderColor: "#38bdf8",
                backgroundColor: "transparent",
                fill: false,
                tension: 0.42,
                borderWidth: 2,
                borderDash: [5, 5],
                pointRadius: 0,
                pointHoverRadius: 4,
                yAxisID: "y1",
              },
            ],
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: { mode: "index", intersect: false },
            animation: { duration: 700, easing: "easeOutQuart" },
            plugins: {
              legend: { display: false },
              tooltip: {
                backgroundColor: "#0f172a",
                titleColor: "#f8fafc",
                bodyColor: "#cbd5e1",
                borderColor: "rgba(148, 163, 184, 0.2)",
                borderWidth: 1,
                padding: 12,
                cornerRadius: 12,
                displayColors: true,
                boxPadding: 4,
                titleFont: { size: 11, weight: "700" },
                bodyFont: { size: 11, weight: "500" },
                callbacks: {
                  label(context) {
                    if (context.datasetIndex === 0) {
                      return ` Ventes : ${compactNumber(context.parsed.y)} M FCFA`;
                    }
                    return ` Commandes : ${context.parsed.y}`;
                  },
                },
              },
            },
            scales: {
              x: {
                grid: { display: false },
                border: { display: false },
                ticks: {
                  color: "#94a3b8",
                  font: { size: 10, weight: "600" },
                  maxRotation: 0,
                },
              },
              y: {
                beginAtZero: true,
                grid: { color: "rgba(148, 163, 184, 0.12)" },
                border: { display: false },
                ticks: {
                  color: "#94a3b8",
                  font: { size: 10, weight: "600" },
                  padding: 8,
                  callback(value) {
                    return compactNumber(value) + " M";
                  },
                },
              },
              y1: {
                position: "right",
                beginAtZero: true,
                grid: { display: false },
                border: { display: false },
                ticks: { display: false },
              },
            },
          },
        });
      },
    }));
  });

  document.addEventListener("keydown", (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
      const search = document.querySelector("[data-global-search]");
      if (search) {
        event.preventDefault();
        search.focus();
        search.select();
      }
    }
  });

  document.body.addEventListener("htmx:responseError", () => {
    window.showToast("Impossible de charger les données. Réessayez.", "error");
  });

  document.body.addEventListener("htmx:sendError", () => {
    window.showToast("Connexion au serveur interrompue.", "error");
  });
})();
