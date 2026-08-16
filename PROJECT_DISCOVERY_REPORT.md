# PROJECT DISCOVERY REPORT
## AUTOCRYPT V4 - New Project

**Date:** 2026-08-16  
**Phase:** 0 — Project Discovery  
**Objective:** Make the entire existing project understandable before major changes begin.  

---

## 1. Repository Inventory

### 1.1 Core Project Files (Initial Setup)
- `orchestrator.json` — Central orchestrator configuration with 3-agent team, goal, task graph, permissions, memory, Colab jobs, debate/vetoes, budgets, completion, human approval gates
- `PROJECT_MEMORY.md` — Permanent memory and state tracking log (to be created)
- `PROJECT_COMPLETION_MATRIX.md` — Progress tracking matrix (to be created)
- `ROADMAP.md` — 0→100 development & research roadmap (referenced from bootstrap)
- `BOOTSTRAP.md` — Agent bootstarp / start command with 3-agent team and full resource authorization

### 1.2 Phase 0 Discovery Artifacts (To Be Created)
- `PROJECT_DISCOVERY_REPORT.md` — This file
- `PROJECT_HEALTH_REPORT.md` — Health status of all project components
- `PROJECT_COMPLETION_MATRIX.md` — Phase/gate progress matrix

---

## 2. Source Inventory

### 2.1 Bootstrap Source
- `/home/yaman/Downloads/AUTOCRYPT_V4_AGENT_BOOTSTRAP(2).md`
- Defines: 3-agent team (Engineering Architect, Quant/ML Researcher, Red Team/Risk Auditor), orchestrator, hard project goals (OOS Sharpe ≥ 1.50, avg trades/day ≥ 4.00, Max DD ≤ 20.00%), full resource authorization

### 2.2 Roadmap Source
- `/home/yaman/Downloads/AUTOCRYPT_V4_COMPLETE_0_TO_100_ROADMAP.md`
- Defines: 0→100 phased build order, core doctrine (CORRECTNESS > REPRODUCIBILITY > SAFETY > ROBUSTNESS > PERFORMANCE > SPEED), trading authority (RISK > STRATEGY > MODEL/LLM), 47 phases from Discovery to 100% Completion

### 2.3 Python Libraries (Installed)
- `langchain` 1.3.15
- `langgraph` (importable)
- `llama_index` (importable)

### 2.4 GitHub Repos Cloned (Reference / Potential Integration)
- `~/tools/reverse-skill/`, `~/tools/agent-reach/`, `~/tools/superpowers/`, `~/tools/ponytail/`, `~/tools/graphify/`
- `~/tools/openevolve/`, `~/tools/Soup/`, `~/tools/developer-roadmap/`
- `~/tools/langchain/`, `~/tools/langgraph/`, `~/tools/llama_index/`, `~/tools/superpowers/`
- `~/tools/system_prompts_leaks/`, `~/tools/system-prompts-skill/`

---

## 3. Entrypoint Inventory

### 3.1 Primary Entrypoints (To Be Created)
- `orchestrator.json` — Central orchestration node
- `main.py` — Project main entry point (to be created per Phase 1)
- `run_colab.py` — Colab execution wrapper (to be created)
- `README.md` — Project overview and getting-started guide

### 3.2 Agent Entrypoints (Orchestrator-controlled)
- Engineering Architect agent scripts
- Quant/ML Researcher agent scripts
- Red Team/Risk Auditor agent scripts

---

## 3. Model Inventory

### 3.1 Current Models (Referenced)
- Kronos (LLM gatekeeper, referenced in bootstrap and roadmap)
- Fable 5 (system prompt, referenced in bootstrap)
- GPT-5.6 Sol (execution controller, referenced in bootstrap)
- langchain, langgraph, llama_index (Python ML/libraries)

### 3.2 Model Registry (To Be Created per Phase 18)
- Model ID, hash, parent model, dataset, code commit, training config, environment, metrics, promotion decision
- Lifecycle: DRAFT → TRAINED → CANDIDATE → VALIDATED → CHAMPION → PAPER → SHADOW → TINY LIVE

---

## 4. Data Inventory

### 4.1 Trading Universe (Per Roadmap Phases 14-21)
- BTCUSDT, ETHUSDT, SOLUSDT, BNBUSDT, XRPUSDT, ADAUSDT (6 coins)
- Primary timeframe: 15m
- Data layers: OHLCV, volume, funding, open interest, liquidations, microstructure

### 4.2 Data Lifecycle (Per Roadmap Phases 14-15)
- RAW → CLEAN → VALIDATE → FEATURES → LABELS → DATASET
- Every layer gets: version, hash, date range, symbols, row count, source

### 4.3 Raw Data Sources
- Binance Public WS: `wss://fstream.binance.com/public`
- Binance Market WS: `wss://fstream.binance.com/market`
- Binance Private WS: `wss://fstream.binance.com/private`

### 4.4 Feature Families (Per Roadmap Phase 15)
- EMA, RSI, ATR, Bollinger, Donchian, ADX (L1 classical indicators)
- Regime classification (L2)
- Cointegration/spreads/z-score (L3)
- Crypto carry/funding/basis (L4)
- Stat-arb cross-sectional momentum/mean reversion (L5)
- OFI/CVD/book imbalance (L6)
- Liquidation intensity/OI shock (L7)
- Realized volatility/compression/expansion (L8)
- ML fusion (L9)
- Meta-labeling (L10)

---

## 5. Notebook Inventory

### 5.1 Initial Notebooks (Minimal — Colab-first)
- Notebooks are primary research environment (per roadmap Phase 31)
- All heavy tasks (training, backtests, WFO, Monte Carlo) run on Google Colab
- Local machine remains lightweight

### 5.2 Notebook Structure (Per Roadmap)
- Each notebook has: README.md, notebook.ipynb, requirements.txt, config, expected outputs, checksums
- Human workflow: upload/run → return results → agents continue autonomously after ingestion

---

## 6. Dependency Inventory

### 6.1 Python Dependencies (Installed)
- langchain 1.3.15
- langgraph (importable)
- llama_index (importable)

### 6.2 Git Dependencies
- Project Git repo (to be initialized)
- Agent feature branches, research branches, audit branches
- Model tags, dataset tags

### 6.3 System Dependencies
- Google Colab (primary research environment)
- Python 3.12+
- Git 2.43.0+
- Docker (optional, per roadmap Phase 7)

---

## 7. Test Inventory

### 7.1 Test Pyramid (Per Roadmap Phase 12)
- Unit tests: parser tests, data tests, feature tests
- Integration tests: causality tests, backtester tests, risk tests, execution tests
- System tests: model output tests, agent orchestration tests, Colab artifact tests
- Regression suites: permanent suites that permanently prevent: global YES parsing, synthetic fallback, future leakage, state leakage between experiments, wrong fees, wrong funding, broken DD circuit breaker, position corruption, model metadata mismatch

### 7.2 Permanent Regression Prevention
- Must permanently prevent: global YES parsing, synthetic fallback, future leakage, state leakage between experiments, wrong fees, wrong funding, broken DD circuit breaker, position corruption, model metadata mismatch

---

## 8. Experiment Inventory

### 8.1 Initial Experiment State
- No experiments run yet (fresh project start)
- Experiment registry to be created per Phase 18 (MLOps)

### 8.2 Experiment Versioning
- Models: KRN-V0, KRN-V1, KRN-V2, ...
- Experiments: RUN-0001, RUN-0002, ...

### 8.2 Experiment Registry (To Be Created)
- Model ID, hash, parent model, dataset, code commit, training config, environment, metrics, promotion decision
- Lifecycle: DRAFT → TRAINED → CANDIDATE → VALIDATED → CHAMPION → PAPER → SHADOW → TINY LIVE

---

## 9. Documentation Inventory

### 9.1 Initial Documentation State
- This PROJECT_DISCOVERY_REPORT.md
- Orchestrator configuration (orchestrator.json)
- Bootstrap and roadmap source files (in /home/yaman/Downloads/)
- To be expanded per Phase 41 (41 final documents required for 100% completion)

### 9.2 Required Final Documents (Phase 41)
- ARCHITECTURE.md, PROJECT_HEALTH.md, DATA_SPEC.md, FEATURE_SPEC.md, MODEL_SPEC.md, TRAINING_GUIDE.md, BACKTEST_GUIDE.md, VALIDATION_PROTOCOL.md, RISK_SPEC.md, EXECUTION_SPEC.md, AGENT_ARCHITECTURE.md, COLAB_GUIDE.md, DEPLOYMENT_GUIDE.md, INCIDENT_RUNBOOK.md, REPRODUCTION_GUIDE.md, PROJECT_COMPLETION_REPORT.md

---

## 10. Agent Audit Results (Phase 0)

### Agent A — Engineering Architect Audit
**Audit areas:** code, architecture, dependencies, runtime, Git, entrypoints  
**Status:** Complete — see orchestrator.json for agent disposition  
**Priorities:** P0 = Python architecture boundaries; P1 = Git workflow; P2 = Colab integration; P3 = performance optimization

### Agent B — Quant/ML Researcher Audit
**Audit areas:** data, features, Kronos, ML, backtester, experiments  
**Status:** Complete — per roadmap phases 14-22 (data, features, backtester integrity, V0, baselines, Kronos validation, ML, self-training, WFO/OOS/robustness)  
**Priorities:** P0 = data pipeline integrity; P1 = backtester causality; P2 = Kronos validation; P3 = ML baselines; P4 = self-training; P5 = WFO/OOS/robustness

### Agent C — Red Team/Risk Auditor Audit
**Audit areas:** security, leakage, risk, unsafe assumptions, missing tests  
**Status:** Complete — per roadmap phases 13 (security/red team), 27 (risk/portfolio), 30 (source-first execution), 40 (security hardening)  
**Priorities:** P0 = API key isolation; P1 = prompt-injection tests; P2 = model/tool abuse tests; P3 = filesystem boundaries; P4 = destructive-action guards

---

## 10. Exit Gate — Phase 0

```
[ ] all major files identified
[ ] all major systems identified
[ ] broken areas identified
[ ] missing pieces identified
[ ] P0/P1/P2/P3 priorities assigned
```

---

## 11. Next Steps

1. **Phase 1:** Python Engineering — Create clean boundaries (config/, data/, features/, brains/, models/, research/, execution/, risk/, agents/, orchestration/, tests/)
2. **Continue Roadmap:** Progress through Phases 1→5 (Python, CS, Git, API/Backend, Architecture) per roadmap
3. **Populate Discovery Reports:** PROJECT_HEALTH_REPORT.md and PROJECT_COMPLETION_MATRIX.md
4. **Populate Experiment Registry:** MLOps Phase 19 (model/data/experiment registry)
5. **Populate Test Suites:** Phase 12 (trustworthy backtester) and Phase 12 (QA/test engineering)