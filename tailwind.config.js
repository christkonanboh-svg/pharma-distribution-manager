/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./core/**/*.py",
    "./static/js/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', "Inter", "Segoe UI", "sans-serif"],
      },
      colors: {
        brand: {
          50: "#effcf9",
          100: "#c9f8ee",
          200: "#94efdd",
          300: "#58e0c8",
          400: "#27c9ae",
          500: "#10ac94",
          600: "#0b8a79",
          700: "#0d6f63",
          800: "#0f5951",
          900: "#104a44",
          950: "#032d2a",
        },
        navy: {
          50: "#f4f6fb",
          100: "#e7eaf3",
          200: "#cbd3e5",
          300: "#a2b0ce",
          400: "#7287b2",
          500: "#516799",
          600: "#3e507d",
          700: "#344166",
          800: "#2e3956",
          900: "#0f172a",
          950: "#080e1d",
        },
      },
      boxShadow: {
        soft: "0 1px 2px rgba(15, 23, 42, 0.04), 0 8px 24px -12px rgba(15, 23, 42, 0.12)",
        lift: "0 2px 4px rgba(15, 23, 42, 0.04), 0 20px 40px -20px rgba(15, 23, 42, 0.24)",
        glow: "0 0 0 1px rgba(16, 172, 148, 0.12), 0 12px 36px -12px rgba(16, 172, 148, 0.5)",
      },
      keyframes: {
        "fade-up": {
          "0%": { opacity: "0", transform: "translateY(12px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        "fade-in": {
          "0%": { opacity: "0" },
          "100%": { opacity: "1" },
        },
        float: {
          "0%, 100%": { transform: "translate3d(0, 0, 0)" },
          "50%": { transform: "translate3d(0, -14px, 0)" },
        },
        shimmer: {
          "0%": { backgroundPosition: "-200% 0" },
          "100%": { backgroundPosition: "200% 0" },
        },
        "slide-in-right": {
          "0%": { opacity: "0", transform: "translateX(24px)" },
          "100%": { opacity: "1", transform: "translateX(0)" },
        },
        "pulse-ring": {
          "0%": { boxShadow: "0 0 0 0 rgba(16, 172, 148, 0.35)" },
          "70%": { boxShadow: "0 0 0 10px rgba(16, 172, 148, 0)" },
          "100%": { boxShadow: "0 0 0 0 rgba(16, 172, 148, 0)" },
        },
        shake: {
          "0%, 100%": { transform: "translateX(0)" },
          "25%": { transform: "translateX(-6px)" },
          "75%": { transform: "translateX(6px)" },
        },
      },
      animation: {
        "fade-up": "fade-up 0.55s cubic-bezier(0.22, 1, 0.36, 1) both",
        "fade-in": "fade-in 0.4s ease-out both",
        float: "float 7s ease-in-out infinite",
        shimmer: "shimmer 2.4s linear infinite",
        "slide-in-right": "slide-in-right 0.35s cubic-bezier(0.22, 1, 0.36, 1) both",
        "pulse-ring": "pulse-ring 2.2s ease-out infinite",
        shake: "shake 0.35s ease-in-out",
      },
    },
  },
  plugins: [],
};
