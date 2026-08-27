# ⚡ ArcPulse // Autonomous Agent Intelligence & Micropayment Stack

An autonomous financial intelligence platform built on the **Arc Testnet** infrastructure, leveraging the **Circle Agent Stack** for instant, low-latency, and cryptographically verified agent-to-agent micro-settlements.

---

## 🌟 Key Features

* **Arc Testnet Native Integration:** Fully pre-configured for the Arc Testnet (Chain ID: `5042002`) using native **USDC** as the gas asset.
* **Auto Network Switching & Provisioning:** Dynamically prompts Web3 wallets (e.g., MetaMask) to switch to or register the Arc Testnet RPC automatically.
* **On-Chain RPC Verification:** Features a dedicated Flask backend endpoint (`/api/verify-tx`) that queries Arc Testnet RPC nodes in real-time to validate transaction execution, block height, and gas consumption before unlocking alpha metrics.
* **xERP Micro-Proof Signatures:** Generates cryptographic proof signatures (`Circle Agent Stack Proof`) upon payment confirmation to ensure secure data delivery.
* **Live Agent Telemetry:** Embedded real-time terminal logger mapping wallet interactions, broadcast events, and RPC verification receipts.

---

## 🛠️ Tech Stack & Architecture

* **Framework:** Python / Flask
* **Frontend:** TailwindCSS, Ethers.js (v5.7)
* **Web3 Ecosystem:** Arc Testnet (Circle L1 Stack), MetaMask
* **Deployment:** Vercel (WSGI Compliant)

---

## 🚀 Network Configuration

| Parameter | Value |
| :--- | :--- |
| **Network Name** | Arc Testnet |
| **Chain ID** | `5042002` (`0x4cef52`) |
| **Native Gas Symbol** | USDC |
| **RPC Endpoint** | `https://rpc.testnet.arc.network` |
| **Block Explorer** | [https://testnet.arcscan.app](https://testnet.arcscan.app) |
| **Testnet Faucet** | [https://faucet.circle.com](https://faucet.circle.com) |

---

## 💻 Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/forumevi/arc-pulse-agent.git](https://github.com/forumevi/arc-pulse-agent.git)
   cd arc-pulse-agent
