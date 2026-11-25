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

  // Impression d'une seule commande : le contenu est cloné dans une feuille
  // dédiée, puis la boîte d'impression native est ouverte. La feuille est
  // retirée dès que la boîte se ferme pour ne pas polluer la page.
  window.printOrder = function (template) {
    if (!template || !template.content) return;

    const sheet = document.createElement("div");
    sheet.className = "print-sheet";
    sheet.appendChild(template.content.cloneNode(true));
    document.body.appendChild(sheet);

    try {
      window.print();
    } finally {
      sheet.remove();
    }
  };

  // Menu latéral : état replié mémorisé, info-bulles et raccourci « [ ».
  document.addEventListener("alpine:init", () => {
    const cartRoot = document.querySelector("[data-client-area]");
    const CART_KEY = (cartRoot && cartRoot.dataset.cartKey) || "dpci.cart";
    const readCart = () => {
      try {
        const stored = JSON.parse(window.localStorage.getItem(CART_KEY) || "[]");
        return Array.isArray(stored) ? stored : [];
      } catch (error) {
        return [];
      }
    };

    // Panier du portail client : persistant, partagé entre les pages.
    Alpine.store("cart", {
      items: readCart(),
      open: false,
      saving: false,
      error: "",

      persist() {
        try {
          window.localStorage.setItem(CART_KEY, JSON.stringify(this.items));
        } catch (error) {}
      },

      get count() {
        return this.items.reduce((sum, item) => sum + item.qty, 0);
      },

      get total() {
        return this.items.reduce((sum, item) => sum + item.price * item.qty, 0);
      },

      add(product) {
        if (!product || Number(product.stock) <= 0) return;
        const line = this.items.find((item) => item.code === product.code);
        if (line) {
          line.qty = Math.min(line.qty + 1, Number(product.stock));
        } else {
          this.items.push({ ...product, qty: 1 });
        }
        this.error = "";
        this.persist();
        this.open = true;
      },

      setQty(code, qty) {
        const line = this.items.find((item) => item.code === code);
        if (!line) return;
        line.qty = Math.min(Math.max(1, Math.round(Number(qty) || 1)), Number(line.stock) || 1);
        this.persist();
      },

      remove(code) {
        this.items = this.items.filter((item) => item.code !== code);
        this.persist();
      },

      clear() {
        this.items = [];
        this.persist();
      },

      openDrawer() {
        this.error = "";
        this.open = true;
      },

      closeDrawer() {
        this.open = false;
      },

      async submit() {
        if (!this.items.length || this.saving) return;

        const root = document.querySelector("[data-client-area]");
        const url = root ? root.dataset.orderUrl : "";
        const token = document.querySelector('meta[name="csrf-token"]');
        this.saving = true;
        this.error = "";

        try {
          const response = await fetch(url, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": token ? token.content : "",
            },
            body: JSON.stringify({
              items: this.items.map((item) => ({ code: item.code, qty: item.qty })),
            }),
          });
          const payload = await response.json();
          if (!response.ok || !payload.ok) {
            throw new Error(payload.error || "La commande n'a pas pu être enregistrée.");
          }
          this.clear();
          this.open = false;
          window.location.assign(payload.redirect);
        } catch (error) {
          this.error = error.message || "Erreur inattendue. Réessayez.";
        } finally {
          this.saving = false;
        }
      },
    });

    Alpine.data("clientArea", () => ({
      money(value) {
        const number = Number(value) || 0;
        return number.toLocaleString("fr-FR", { maximumFractionDigits: 0 }) + " F";
      },
    }));

    Alpine.data("layout", () => ({
      sidebarOpen: false,
      collapsed: false,
      tip: null,
      tipTop: 0,

      init() {
        this.collapsed = document.documentElement.classList.contains("sidebar-collapsed");
        window.addEventListener("resize", () => {
          if (window.innerWidth < 1024) this.hideTip();
        });
      },

      toggleSidebar() {
        this.collapsed = !this.collapsed;
        document.documentElement.classList.toggle("sidebar-collapsed", this.collapsed);
        try {
          window.localStorage.setItem("dpci.sidebar", this.collapsed ? "collapsed" : "expanded");
        } catch (error) {}
        this.hideTip();
      },

      showTip(event) {
        if (!this.collapsed || window.innerWidth < 1024) return;
        const item = event.target.closest("[data-tip]");
        if (!item) return;
        const rect = item.getBoundingClientRect();
        this.tip = item.dataset.tip;
        this.tipTop = Math.round(rect.top + rect.height / 2);
      },

      hideTip() {
        this.tip = null;
      },
    }));

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
        Chart.defaults.color = "#64748b";

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
                borderWidth: 2,
                pointRadius: 0,
                pointHoverRadius: 4,
                pointHoverBackgroundColor: "#ffffff",
                pointHoverBorderColor: "#0b8a79",
                pointHoverBorderWidth: 2,
              },
              {
                label: "Commandes",
                data: series.orders,
                borderColor: "#7287b2",
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
                cornerRadius: 8,
                displayColors: true,
                boxPadding: 4,
                titleFont: { size: 11, weight: "600" },
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
                  color: "#64748b",
                  font: { size: 10, weight: "500" },
                  maxRotation: 0,
                },
              },
              y: {
                beginAtZero: true,
                grid: { color: "rgba(148, 163, 184, 0.16)" },
                border: { display: false },
                ticks: {
                  color: "#64748b",
                  font: { size: 10, weight: "500" },
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

    if (
      event.key === "[" &&
      !event.metaKey &&
      !event.ctrlKey &&
      !event.altKey &&
      window.innerWidth >= 1024
    ) {
      const target = event.target;
      const typing =
        target &&
        (["INPUT", "TEXTAREA", "SELECT"].includes(target.tagName) || target.isContentEditable);
      if (typing || !window.Alpine) return;

      const root = document.querySelector("[data-app-layout]");
      const state = root ? window.Alpine.$data(root) : null;
      if (state && typeof state.toggleSidebar === "function") {
        event.preventDefault();
        state.toggleSidebar();
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
