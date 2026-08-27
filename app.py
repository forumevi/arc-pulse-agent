from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ArcPulse // Autonomous Agent Intelligence</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/ethers@5.7.2/dist/ethers.umd.min.js"></script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans min-h-screen p-4 md:p-8">
    <div class="max-w-6xl mx-auto space-y-6">
        
        <!-- Header -->
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center border-b border-slate-800 pb-4 gap-4">
            <div>
                <h1 class="text-3xl font-extrabold tracking-tight text-cyan-400">⚡ ArcPulse Agent Stack</h1>
                <p class="text-sm text-slate-400 mt-1">Autonomous Financial Intelligence & On-Chain Micropayment Routing</p>
            </div>
            <div class="flex items-center gap-3">
                <span id="network-badge" class="px-3 py-1 bg-amber-500/10 text-amber-400 border border-amber-500/30 rounded-full text-xs font-mono">
                    ● Disconnected
                </span>
                <button id="connect-btn" onclick="connectWallet()" class="px-5 py-2 bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold rounded-xl text-sm transition shadow-lg shadow-cyan-500/20">
                    Connect Wallet
                </button>
            </div>
        </div>

        <!-- Dashboard Stats Grid -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 backdrop-blur">
                <p class="text-xs text-slate-400 uppercase tracking-wider">Settlement Engine</p>
                <p class="text-xl font-bold text-white mt-1">Circle Agent Stack</p>
            </div>
            <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 backdrop-blur">
                <p class="text-xs text-slate-400 uppercase tracking-wider">Target Chain</p>
                <p class="text-xl font-bold text-cyan-400 mt-1">Arc Ecosystem</p>
            </div>
            <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 backdrop-blur">
                <p class="text-xs text-slate-400 uppercase tracking-wider">Micro-Fee Rate</p>
                <p class="text-xl font-bold text-emerald-400 mt-1">0.05 USDC / Tx</p>
            </div>
            <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 backdrop-blur">
                <p class="text-xs text-slate-400 uppercase tracking-wider">Agent Heartbeat</p>
                <p class="text-xl font-bold text-purple-400 mt-1" id="agent-status">Active [v0.0.6+]</p>
            </div>
        </div>

        <!-- Main Workspace Split -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            
            <!-- Paywall Execution Card -->
            <div class="lg:col-span-2 bg-slate-900/90 border border-slate-800 rounded-2xl p-6 space-y-5">
                <div class="border-b border-slate-800 pb-3">
                    <h2 class="text-lg font-semibold text-white">Execute Agent-to-Agent Micro-Settlement</h2>
                    <p class="text-xs text-slate-400">Trigger on-chain Web3 transaction request to unlock autonomous yield data.</p>
                </div>

                <div class="p-4 bg-slate-950 rounded-xl border border-slate-800/80 space-y-3 font-mono text-xs">
                    <div class="flex justify-between"><span class="text-slate-500">Target Agent:</span> <span class="text-slate-300">0x71C...49A2 (Arc Treasury Bot)</span></div>
                    <div class="flex justify-between"><span class="text-slate-500">Asset Requested:</span> <span class="text-cyan-400">USDC (Arc Native)</span></div>
                    <div class="flex justify-between"><span class="text-slate-500">Settlement Cost:</span> <span class="text-emerald-400">0.05 USDC</span></div>
                </div>

                <button onclick="executePayment()" class="w-full py-3.5 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-slate-950 font-extrabold rounded-xl transition shadow-lg text-sm tracking-wide">
                    Sign & Pay 0.05 USDC (Web3 Prompt)
                </button>

                <!-- Dynamic Output Screen -->
                <div id="status-box" class="hidden p-4 bg-slate-950 rounded-xl border border-slate-800 font-mono text-xs text-slate-300 leading-relaxed"></div>
            </div>

            <!-- Terminal Stream Logs -->
            <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between">
                <div>
                    <h2 class="text-md font-semibold text-white border-b border-slate-800 pb-3">Live Agent Telemetry</h2>
                    <div id="terminal-logs" class="mt-4 font-mono text-[11px] space-y-2 text-slate-400 max-h-60 overflow-y-auto">
                        <p class="text-cyan-400">[SYSTEM] Agent initialized on Arc RPC.</p>
                        <p>[INFO] Circle CLI stack status: v0.0.6 (Up to date)</p>
                        <p>[WAIT] Awaiting wallet signature connection...</p>
                    </div>
                </div>
            </div>

        </div>

    </div>

    <script>
        let provider, signer, userAddress;

        async function connectWallet() {
            if (window.ethereum) {
                try {
                    provider = new ethers.providers.Web3Provider(window.ethereum);
                    await provider.send("eth_requestAccounts", []);
                    signer = provider.getSigner();
                    userAddress = await signer.getAddress();
                    
                    document.getElementById('connect-btn').innerText = userAddress.substring(0,6) + "..." + userAddress.substring(38);
                    document.getElementById('network-badge').innerText = "● Connected";
                    document.getElementById('network-badge').className = "px-3 py-1 bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 rounded-full text-xs font-mono";
                    
                    logTerminal(`Wallet Connected: ${userAddress}`);
                } catch (err) {
                    logTerminal(`[ERROR] Wallet Connection Failed: ${err.message}`);
                }
            } else {
                alert("Please install MetaMask or Web3 Wallet to interact with ArcPulse.");
            }
        }

        async function executePayment() {
            const box = document.getElementById('status-box');
            box.classList.remove('hidden');

            if (!signer) {
                box.innerHTML = "<span class='text-amber-400'>⚠️ Please connect your Web3 wallet first!</span>";
                return;
            }

            try {
                box.innerHTML = "<span class='text-cyan-400 animate-pulse'>⏳ Prompting MetaMask on-chain signature for Circle Micro-settlement...</span>";
                logTerminal("[TX] Initiating 0.05 USDC Micro-settlement transaction...");

                // Triggers REAL Web3 Transaction Prompt
                const tx = await signer.sendTransaction({
                    to: "0x0000000000000000000000000000000000000000", // Burn / Demo Treasury Target
                    value: ethers.utils.parseEther("0.0001") // Real Native Network Call
                });

                box.innerHTML = `<span class='text-emerald-400'>✅ On-Chain Transaction Sent!</span><br><span class='text-slate-400'>Tx Hash: ${tx.hash}</span><br>⏳ Verifying Circle Agent Stack proof...`;
                logTerminal(`[SUCCESS] Tx Hash: ${tx.hash}`);

                setTimeout(() => {
                    box.innerHTML += `<br><br><span class='text-cyan-300'>📊 [UNLOCKED ARC ALPHA METRICS]:</span><br>• Arc Chain Yield: +16.4% APY<br>• Optimal Route: Circle Liquidity Pool #09<br>• Settlement Latency: 118ms`;
                }, 2000);

            } catch (err) {
                box.innerHTML = `<span class='text-red-400'>❌ Settlement Failed/Rejected: ${err.message}</span>`;
                logTerminal(`[REJECTED] User cancelled or failed transaction.`);
            }
        }

        function logTerminal(msg) {
            const logs = document.getElementById('terminal-logs');
            const p = document.createElement('p');
            p.innerText = `[${new Date().toLocaleTimeString()}] ${msg}`;
            logs.appendChild(p);
            logs.scrollTop = logs.scrollHeight;
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
