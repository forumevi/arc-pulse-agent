from flask import Flask, render_template_string, jsonify
import time
import random

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ArcPulse // Agent Intelligence</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans p-8">
    <div class="max-w-5xl mx-auto space-y-6">
        <!-- Header -->
        <div class="flex justify-between items-center border-b border-slate-800 pb-4">
            <div>
                <h1 class="text-2xl font-bold tracking-wide text-cyan-400">⚡ ArcPulse Agent Stack</h1>
                <p class="text-xs text-slate-400">Autonomous Financial Intelligence on Arc & Circle USDC</p>
            </div>
            <span class="px-3 py-1 bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 rounded-full text-xs animate-pulse">
                ● Live Agent Network
            </span>
        </div>

        <!-- Metrics Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="bg-slate-900 border border-slate-800 rounded-xl p-4">
                <p class="text-xs text-slate-400">24h Settlement Volume</p>
                <p class="text-2xl font-bold text-white mt-1">$142,850 <span class="text-xs text-slate-500">USDC</span></p>
            </div>
            <div class="bg-slate-900 border border-slate-800 rounded-xl p-4">
                <p class="text-xs text-slate-400">Active Arc Agents</p>
                <p class="text-2xl font-bold text-cyan-400 mt-1">1,248</p>
            </div>
            <div class="bg-slate-900 border border-slate-800 rounded-xl p-4">
                <p class="text-xs text-slate-400">Avg. Micropay Latency</p>
                <p class="text-2xl font-bold text-emerald-400 mt-1">120ms</p>
            </div>
        </div>

        <!-- Demo Action Panel -->
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-6 text-center space-y-4">
            <h2 class="text-lg font-semibold">Request Premium AI Agent Insights</h2>
            <p class="text-xs text-slate-400 max-w-md mx-auto">Execute Circle USDC micro-settlement (0.05 USDC) to unlock deep-level Arc ecosystem treasury prediction data.</p>
            <button onclick="triggerPayment()" class="px-6 py-2.5 bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-semibold rounded-lg text-sm transition">
                Pay 0.05 USDC & Fetch Data
            </button>
            <div id="status-box" class="hidden p-3 bg-slate-950 rounded border border-slate-800 text-xs font-mono text-cyan-300"></div>
        </div>
    </div>

    <script>
        function triggerPayment() {
            const box = document.getElementById('status-box');
            box.classList.remove('hidden');
            box.innerHTML = "⏳ Initiating Circle Agent Stack USDC payment routing...";
            
            setTimeout(() => {
                box.innerHTML = "✅ Payment Verified on-chain! Fetching Arc agent metrics...";
                setTimeout(() => {
                    box.innerHTML = "📊 [PREMIUM DATA UNLOCKED]: Arc Treasury Yield Alpha: +14.2% | Recommended Route: Circle Yield Pool #04";
                }, 1200);
            }, 1500);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
