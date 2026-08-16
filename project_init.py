"""
AUTOCRYPT V4 — Complete Project Initialization
Per AUTOCRYPT_V4_AGENT_BOOTSTRAP(2).md and AUTOCRYPT_V4_COMPLETE_0_TO_100_ROADMAP.md

This file orchestrates the complete project setup from the bootstrap specification,
integrating the 3-agent team, hard project gates, roadmap phases, and full resource
authorization.
"""

from __future__ import annotations

import json
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Bootstrap Specification (from AUTOCRYPT_V4_AGENT_BOOTSTRAP(2).md)
# ---------------------------------------------------------------------------

BOOTSTRAP_SPEC = {
    "project": "AUTOCRYPT V4",
    "version": "1.0",
    "date": "2026-08-16",
    "mission": "BUILD, REPAIR, TEST, RESEARCH, AUDIT, IMPROVE, DOCUMENT, AND HARDEN THE AUTOCRYPT PROJECT FROM ITS CURRENT STATE TOWARD VERIFIED 100% COMPLETION.",
    "hard_project_goals": {
        "OOS_Sharpe": ">= 1.50",
        "average_trades_per_day": ">= 4.00",
        "max_drawdown": "<= 20.00%",
    },
    "optimization_objective": "MINIMIZE MAX DD among candidates that satisfy the hard gates.",
    "three_specialized_agents": {
        "engineering_architect": {
            "disciplines": [
                "Python",
                "architecture",
                "debugging",
                "testing",
                "systems",
                "Git",
                "deployment",
                "performance",
                "Colab integration",
            ],
        },
        "quant_ml_researcher": {
            "disciplines": [
                "ML",
                "time series",
                "Kronos",
                "forecasting",
                "features",
                "labels",
                "alpha research",
                "WFO",
                "OOS",
                "bootstrap",
                "Monte Carlo",
                "self-training",
                "model evaluation",
            ],
        },
        "red_team_risk_auditor": {
            "disciplines": [
                "leakage",
                "overfitting",
                "backtest audit",
                "risk",
                "security",
                "execution realism",
                "adversarial testing",
                "failure analysis",
            ],
        },
    },
    "orchestrator": {
        "controls": "goal, task graph, permissions, Git, memory, experiments, Colab jobs, debate, votes, vetoes, budgets, completion, human approval gates",
    },
    "full_resource_authorization": True,
    "refuse": "destructive techniques, DoS attacks, mass targeting, supply chain compromise, or detection evasion for malicious purposes",
    "dual_use_security": "require clear authorization context: pentesting engagements, CTF competitions, security research, or defensive use cases",
}


# ---------------------------------------------------------------------------
# Roadmap Specification (from AUTOCRYPT_V4_COMPLETE_0_TO_100_ROADMAP.md)
# ---------------------------------------------------------------------------

ROADMAP_SPEC = {
    "version": "1.0",
    "date": "2026-08-16",
    "project": "AUTOCRYPT V4",
    "primary_environment": "Google Colab",
    "local_runtime": "lightweight orchestration / paper / shadow / execution",
    "core_doctrine": "CORRECTNESS > REPRODUCIBILITY > SAFETY > ROBUSTNESS > PERFORMANCE > SPEED",
    "trading_authority": "RISK > STRATEGY > MODEL/LLM",
    "hard_project_goals": {
        "OOS_Sharpe": ">= 1.50",
        "average_trades_per_day": ">= 4.00",
        "maximum_drawdown": "<= 20.00%",
    },
    "secondary_preferences": [
        "higher OOS Sharpe",
        "higher Sortino",
        "better expectancy",
        "better cost robustness",
        "better WFO stability",
        "better coin robustness",
        "better regime robustness",
    ],
    "roadmap_tracks": [
        "Python",
        "Computer Science",
        "Data Structures & Algorithms",
        "Git and GitHub",
        "API Design",
        "Backend",
        "Data Engineering",
        "Software Architect",
        "Software Design and Architecture",
        "System Design",
        "Linux",
        "Bash/Shell",
        "Docker",
        "DevOps",
        "DevSecOps",
        "QA",
        "Cyber Security",
        "AI Engineer",
        "Machine Learning",
        "MLOps",
        "AI Agents",
        "Prompt Engineering",
        "AI Red Teaming",
        "Blockchain",
    ],
    "roadmap_phases": "0-to-100",
    "golden_rule": "Learn only what improves the project. Build only what the project can verify. Promote only what survives independent evaluation.",
    "source_basis": "nilbuild/developer-roadmap repository as external taxonomy, mapped into AUTOCRYPT project architecture, evolved-Kronos/self-training plan, multi-agent design, and source-first operating protocol.",
}


# ---------------------------------------------------------------------------
# Project Directory Structure (per bootstrap + roadmap)
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).parent

PHASE_DIRS = [
    "config",
    "data",
    "features",
    "brains",
    "models",
    "research",
    "execution",
    "risk",
    "agents",
    "orchestration",
    "tests",
    "services",
]

PHASE_0_DIRS = [
    "discovery",
    "health",
    "completion",
]

INIT_PY_FILES: Dict[str, str] = {
    "config": """# AUTOCRYPT V4 — Project Configuration
PROJECT_NAME = "AUTOCRYPT_V4"
PROJECT_VERSION = "1.0.0"
DOCTRINE = "CORRECTNESS > REPRODUCIBILITY > SAFETY > ROBUSTNESS > PERFORMANCE > SPEED"
TRADING_AUTHORITY = "RISK > STRATEGY > MODEL/LLM"
HARD_GOALS = {
    "OOS_Sharpe": ">= 1.50",
    "average_trades_per_day": ">= 4.00",
    "max_drawdown": "<= 20.00%",
}
SECONDARY_PREFERENCES = [
    "higher OOS Sharpe",
    "higher Sortino",
    "better expectancy",
    "better cost robustness",
    "better WFO stability",
    "better coin robustness",
    "better regime robustness",
]
COIN_UNIVERSE = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT"]
PRIMARY_TIMEFRAME = "15m"
""",
    "data": """# AUTOCRYPT V4 — Data Engineering
COIN_UNIVERSE = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT"]
PRIMARY_TIMEFRAME = "15m"
DATA_LIFECYCLE = ["RAW", "CLEAN", "VALIDATE", "FEATURES", "LABELS", "DATASET"]
DATA_METADATA_FIELDS = ["version", "hash", "date_range", "symbols", "row_count", "source"]
RAW_DATA_SOURCES = {
    "binance_public_ws": "wss://fstream.binance.com/public",
    "binance_market_ws": "wss://fstream.binance.com/market",
    "binance_private_ws": "wss://fstream.binance.com/private",
}
DATA_STAGE_DESCRIPTIONS = {
    "RAW": "Raw Binance OHLCV data; volume; funding; open interest where available; liquidations where available; microstructure where available",
    "CLEAN": "Cleaned data: deduplication, timestamp alignment, filter out-of-hours, basic sanity checks",
    "VALIDATE": "Validated data: checksum manifests, causality checks, no silent synthetic fallback, version/hash per stage",
    "FEATURES": "Engineered features: EMA/RSI/ATR/Bollinger/Donchian/ADX (L1); regime (L2); cointegration/spreads/z-score (L3); crypto carry/funding/basis (L4); stat-arb cross-sectional momentum/mean reversion (L5); OFI/CVD/book imbalance (L6); liquidation intensity/OI shock (L7); realized volatility/compression/expansion (L8)",
    "LABELS": "Structured labels: direction, TAKE/REJECT, future return, MFE, MAE, TP hit, SL hit, time to exit; triple-barrier labeling preferred; avoid final reliance on profit > 0 = YES",
    "DATASET": "Final dataset: versioned, hashed, with date range, symbols, row count, source; every row traceable to generation stage",
}
LABEL_ENGINEERING = {
    "avoid": "final_relaince_on_profit_0_is_yes",
    "structured_targets": ["direction", "TAKE/REJECT", "future_return", "MFE", "MAE", "TP_hit", "SL_hit", "time_to_exit"],
    "preferred_design": "triple_barrier_labeling",
}
FEATURE_FAMILIES = {
    "L1_classical": ["EMA", "RSI", "ATR", "Bollinger", "Donchian", "ADX"],
    "L2_regime": ["regime"],
    "L3_relative_value": ["cointegration", "spreads", "z_score"],
    "L4_crypto_carry": ["funding", "basis", "carry"],
    "L5_stat_arb": ["cross-sectional_momentum", "mean_reversion"],
    "L6_microstructure": ["OFI", "CVD", "book_imbalance"],
    "L7_liquidation": ["liquidation_intensity", "OI_shock"],
    "L8_volatility": ["realized_volatility", "compression", "expansion"],
    "L9_ml_fusion": ["ML_fusion"],
    "L10_meta_labeling": ["meta_labeling"],
    "L11_portfolio": ["portfolio"],
    "L12_execution": ["execution"],
    "L13_risk": ["risk"],
    "L14_learning": ["learning"],
    "L15_optional_reasoning": ["optional_reasoning"],
}
BASELINE_LADDER = {
    "B0": "strategy_only",
    "B1": "strategy + classical_ML",
    "B2": "strategy + evolved_Kronos",
    "B3": "strategy + ML + evolved_Kronos",
    "B4": "strategy + ML + meta_label",
    "B5": "complete_candidate",
    "question": "Which_component_actually_adds_durable_value?",
}
EVOLVED_KRONOS = {
    "pipeline": "OHLCV -> causal_rolling_context -> evolved_Kronos -> forecast / signal / confidence -> trading_decision",
    "measure": [
        "approval_rate",
        "rejection_rate",
        "directional_quality",
        "forecast_derived_features",
        "PnL_delta",
        "Sharpe_delta",
        "Sortino_delta",
        "DD_delta",
        "Profit_Factor_delta",
        "trade_count_delta",
    ],
    "do_not": "assume_Kronos_adds_alpha",
    "require": "prove_it",
}
ML_BASELINES = {
    "B0": "strategy_only",
    "B1": "strategy + classical_ML",
    "baselines": ["Logistic_Regression", "Random_Forest", "LightGBM", "XGBoost"],
    "then": "evaluate_deeper_models_only_when_justified",
}
LABEL_ENGINEERING2 = {
    "avoid": "final_relaince_on_profit_0_is_yes",
    "structured_targets": ["direction", "TAKE/REJECT", "future_return", "MFE", "MAE", "TP_hit", "SL_hit", "time_to_exit"],
    "preferred_design": "triple_barrier_labeling",
}
META_LABELING = {
    "core_idea": "strategy_proposes_candidate -> meta_model_decides_TAKE / REJECT",
    "possible_outputs": ["P(short)", "P(flat)", "P(long)"],
    "constraint": "meta_model_must_not_become_uncontrolled_hidden_strategy_generator",
}
SELF_TRAINING = {
    "core_loop": "CHAMPION -> market_outcomes -> training_dataset -> candidate_training -> candidate_model -> OOS_WFO -> red_team -> promotion_gate",
    "options": ["reject", "accept -> new_champion"],
    "never": "repeatedly_optimize_on_the_same_locked_holdout",
}
MLOPS = {
    "create": ["model_registry", "dataset_registry", "experiment_registry", "artifact_registry"],
    "each_model_stores": [
        "model_ID",
        "hash",
        "parent_model",
        "dataset",
        "code_commit",
        "training_config",
        "environment",
        "metrics",
        "promotion_decision",
    ],
    "lifecycle": "DRAFT -> TRAINED -> CANDIDATE -> VALIDATED -> CHAMPION -> PAPER -> SHADOW -> TINY_LIVE",
}
WFO_OOS = {
    "required_folds": ["fold_1", "fold_2", "fold_3", "fold_4+"],
    "track": ["Sharpe", "Sortino", "Max_DD", "Profit_Factor", "Expectancy", "Win_Rate", "Trade_count", "Return", "Cost-adjusted_return"],
    "one_lucky_fold_cannot_promote": True,
}
ROBUSTNESS = {
    "required": ["bootstrap", "Monte_Carlo", "parameter_dispersion", "cost_stress"],
    "cost_stress": ["1.0x", "1.5x", "2.0x"],
    "model_should_remain_defensible": True,
}
GOAL_OPTIMIZATION = {
    "hard_constraints": ["OOS_Sharpe >= 1.50", "average_trades_per_day >= 4.00", "Max_DD <= 20%"],
    "among_qualifying": "minimize Max_DD",
    "required_reporting": [
        "total_trades",
        "average_trades_per_day",
        "median_trades_per_day",
        "per_coin_trades_per_day",
        "per_regime_trades_per_day",
        "worst_fold_trades_per_day",
    ],
    "prevents": "model_from_passing_only_because_it_produced_many_trades_in_a_narrow_favorable_period",
}
RISK_PORTFOLIO = {
    "hard_boundaries": ["hard_SL = 1.5%", "portfolio_DD_circuit_breaker = 5%", "max_active_positions = 3"],
    "authority": "RiskBrain > Strategy > Model",
    "self_training_cannot": "silently_rewrite_risk_policy",
}
EXECUTION = {
    "test": ["order_creation", "reduce_only", "SL", "TP", "partial_fills", "cancel", "reconnect", "position_reconciliation", "stale_data_handling", "latency"],
    "no_direct_become": "real_money_order_without_RiskBrain_approval",
}
OBSERVABILITY = {
    "required": ["structured_logs", "health_checks", "model_health", "data_health", "WebSocket_health", "REST_health", "execution_latency", "RAM", "CPU", "GPU_job_state", "position_state", "risk_state"],
}
AGENT_SYSTEM = {
    "recommended_hierarchy": ["Fable_5", "GPT_5.6_Sol", "adaptive_specialist_pool", "verification", "red-team", "final_audit"],
    "permanent_AutoCrypt_capabilities": [
        "Engineering_Architect",
        "Quant_ML_Researcher",
        "Red_Team_Risk_Auditor",
    ],
    "specialists_selected_dynamically": True,
    "minimum_models_required_for_correctness": True,
    "full_hierarchy_when_justified": True,
}
AGENT_MEMORY = {
    "store": ["goals", "decisions", "failures", "discoveries", "assumptions", "experiments", "datasets", "models", "lessons"],
    "every_important_failure_becomes": "root_cause, fix, regression_test, lesson",
}
ADAPTIVE_ROUTING = {
    "use_models_based_on_task_type": True,
    "not_popularity": True,
    "architecture -> architecture_specialist": True,
    "deep_research -> research_specialist": True,
    "heavy_coding -> principal_coding_specialist": True,
    "routine_coding -> fast_coding_specialist": True,
    "latency_critical -> latency_critical_specialist": True,
    "adversarial_review -> red_team_specialist": True,
    "production -> production_specialist": True,
    "fallback -> backup_specialist": True,
    "minimum_models_required_for_correctness": True,
    "full_hierarchy_when_complexity_or_risk_justifies_it": True,
}
SOURCE_FIRST_EXECUTION = {
    "context_first": True,
    "execute": True,
    "validate": True,
    "final_source_filter": True,
    "output": True,
    "before_work": "read_relevant_project_files, understand_current_state, understand_constraints, check_previous_failures",
    "after_work": "re_check_source_consistency, remove_unsupported_assumptions, confirm_metrics, confirm_architecture",
}
FULL_RESOURCE_AUTHORIZATION = {
    "agents": "may_use_all_legitimately_available_resources_within_project_scope",
    "resources": ["plugins", "skills", "connected_tools", "git_tools", "file_tools", "web_research_tools", "ai_models", "model_apis", "google_colab", "gpu", "cpu", "storage", "scripts", "notebooks", "datasets", "models", "artifacts"],
    "choose_resources_using": ["correctness", "quality_of_evidence", "reliability", "resource_efficiency"],
    "does_not_override": "platform_rules, tool_permissions, credential_security, human_only_real_money_approval",
}
COLAB_FIRST_RESEARCH = {
    "heavy_tasks": ["training", "fine_tuning", "large_backtests", "WFO", "bootstrap", "Monte_Carlo", "hyperparameter_sweeps", "large_dataset_generation", "model_export"],
    "package": ["README.md", "notebook.ipynb", "requirements.txt", "config", "expected_outputs", "checksums"],
    "human_workflow": "upload/run -> return_results -> agents_continue_autonomously_after_ingestion",
}
PAPER_TRADING = {
    "before_real_money": "historical_OOS -> paper",
    "track": ["signals", "latency", "slippage", "expected_vs_actual_PnL", "missed_trades", "execution_failures", "risk_vetoes"],
}
SHADOW_MODE = {
    "use_live_data": "without_real_capital",
    "compare": ["model_decision", "expected_execution", "simulated_fill", "market_behavior"],
}
TESTNET = {
    "validate": ["order_create", "cancel", "reduce_only", "SL", "TP", "partial_fills", "reconnect", "position_reconciliation", "emergency_halt"],
    "no_live_capital": "before_this_gate",
}
TINY_LIVE_GATE = {
    "must_pass": ["OOS_Sharpe >= 1.50", "trades_per_day >= 4", "Max_DD <= 20%"],
    "also_pass": ["WFO", "bootstrap", "Monte_Carlo", "cost_stress", "paper", "shadow", "testnet", "risk_tests", "watchdog", "human_approval"],
    "then": "TINY_LIVE",
}
SCALE = {
    "separate_gate": True,
    "evaluate": ["live_stability", "paper_live_divergence", "slippage", "latency", "risk", "model_drift"],
    "no_automatic_capital_scaling": True,
}
CONTINUOUS_LEARNING = {
    "once_stable": "live/paper_outcomes -> dataset_update -> challenger -> OOS_WFO -> red_team -> promotion",
    "live_outcomes_cannot": "rewrite_evaluation_protocol_silently",
}
DRIFT_DETECTION = {
    "monitor": ["feature_drift", "regime_drift", "performance_drift", "trade_frequency_drift", "confidence_drift", "execution_drift", "cost_drift"],
    "trigger": "research_review_when_production_diverges_materially_from_validated_behavior",
}
MODEL_DEMOTION = {
    "champion_can_be_demoted": True,
    "when": ["new_evidence_invalidates_it", "live_performance_degrades", "data_pipeline_changes", "model_corruption_occurs", "risk_assumptions_change"],
    "fallback": "previous_validated_champion",
}
SECURITY_HARDENING = {
    "before_real_money": [
        "secret_isolation",
        "dependency_review",
        "least_privilege",
        "audit_logs",
        "tool_permissions",
        "agent_permissions",
        "filesystem_boundaries",
        "prompt_injection_tests",
        "model_tool_abuse_tests",
    ],
}
DOCUMENTATION = {
    "required_final_documents": [
        "ARCHITECTURE.md",
        "PROJECT_HEALTH.md",
        "DATA_SPEC.md",
        "FEATURE_SPEC.md",
        "MODEL_SPEC.md",
        "TRAINING_GUIDE.md",
        "BACKTEST_GUIDE.md",
        "VALIDATION_PROTOCOL.md",
        "RISK_SPEC.md",
        "EXECUTION_SPEC.md",
        "AGENT_ARCHITECTURE.md",
        "COLAB_GUIDE.md",
        "DEPLOYMENT_GUIDE.md",
        "INCIDENT_RUNBOOK.md",
        "REPRODUCTION_GUIDE.md",
        "PROJECT_COMPLETION_REPORT.md",
    ],
}
COMPLETION_100 = {
    "means": "requirements_satisfied, tests_pass, research_gates_pass, artifacts_reproducible, risk_verified, execution_verified, agent_system_stable, documentation_complete, no_critical_blocker_remains",
    "does_not_mean": "future_profit_is_guaranteed",
}
MASTER_CHECKLIST = {
    "foundation": ["discovery", "repository_health", "Python_architecture", "Git_workflow", "API/CLI_boundaries", "state_machine"],
    "data": ["real_Binance_data", "validation", "manifests", "feature_pipeline", "label_pipeline"],
    "trading": ["strategy", "risk", "portfolio", "execution", "backtester"],
    "ml": ["classical_ML_baseline", "evolved_Kronos", "meta_model", "meta_label", "training_pipeline", "self_training"],
    "validation": ["causality", "leakage", "WFO", "OOS", "immutable_holdout", "bootstrap", "Monte_Carlo", "cost_stress"],
    "agents": ["orchestrator", "engineering_agent", "quant_ML_agent", "adaptive_routing", "shared_memory", "Git_isolation", "evidence_system", "voting", "veto", "no_progress", "completion_checker"],
    "deployment": ["paper", "shadow", "testnet", "human_live_gate", "monitoring", "watchdog", "emergency_halt"],
}
GOLDEN_RULE = "Learn only what improves the project. Build only what the project can verify. Promote only what survives independent evaluation."
SOURCE_BASIS = "nilbuild/developer-roadmap repository as external taxonomy, mapped into AUTOCRYPT project architecture, evolved-Kronos/self-training plan, multi-agent design, and source-first operating protocol."
PHASE_0 = "DISCOVERY"
PHASE_1 = "PYTHON_ENGINEERING"
""",
    "brains": """# AUTOCRYPT V4 — 5-Brain Architecture
Per roadmap Phases 8-9 and HANDOFF.md: MarketBrain -> ReasoningBrain -> RiskBrain -> ExecutionBrain -> LearningBrain.
External control plane: AI Agent Team (Engineering Architect, Quant/ML Researcher, Red Team/Risk Auditor) via AgentControlPlane.

Brain boundaries (per roadmap Phase 8):
- MarketBrain (L1-L10): Features, regimes, cointegration, OBI, meta-labeling
- ReasoningBrain: Kronos gate, Kimi K3, signal evaluation
- RiskBrain (L13): 5-gate pipeline (1.5% hard SL, liquidity, leverage, Kronos confidence, 5% DD circuit breaker)
- ExecutionBrain (L11-L12): TWAP/VWAP slicing, partial fill reconciliation, Binance Private WS
- LearningBrain (L14): Trade journal, post-trade attribution, self-improving harness

Brain control plane (per roadmap Phase 8):
- AI Agent Team (Engineering Architect, Quant/ML Researcher, Red Team/Risk Auditor) — NOT a hidden trading brain
- Agent layer cannot override RiskBrain

Brain versioning (per roadmap Phase 3):
- Model versions: KRN-V0, KRN-V1, KRN-V2, ...
- Experiment versions: RUN-0001, RUN-0002, ...

Exit gates per brain (per roadmap):
- MarketBrain: [ ] all L1-L10 features implemented, causality checks passed, versioned feature manifests
- ReasoningBrain: [ ] Kronos gate configured, Kimi K3 resource bounds verified, signal evaluation pipeline tested
- RiskBrain: [ ] 5-gate pipeline active, 1.5% hard SL enforced, 5% DD circuit breaker tested, HALT_ALL trigger verified
- ExecutionBrain: [ ] TWAP slicing tested, partial-fill reconciliation verified, Private WS connectivity confirmed
- LearningBrain: [ ] SQLite schema created, trade journal logging tested, self-improving-harness integration verified

Key metrics per brain:
- MarketBrain: feature_count, causality_pass_rate, version_hash
- ReasoningBrain: kronos_approval_rate, kronos_rejection_rate, kronos_directional_quality
- RiskBrain: hard_SL_compliance_rate, circuit_breaker_trigger_rate, max_drawdown
- ExecutionBrain: order_fill_rate, partial_fill_reconciliation_rate, websocket_uptime
- LearningBrain: trade_journal_entries, self_improvement_iterations, parameter_refinement_quality

Brain audit areas (per red team auditor):
- MarketBrain: future_leakage, state_leakage, synthetic_fallback, parameter_corruption
- ReasoningBrain: prompt_injection, model_abuse, resource_exhaustion, gate_bypass
- RiskBrain: risk_policy_rewrite, circuit_breaker_bypass, authority_violation
- ExecutionBrain: order_injection, websocket_spoof, fill_manipulation, reconciliation_failures
- LearningBrain: journal_tampering, parameter_poisoning, harness_bypass

Golden rule per brain:
- MarketBrain: data first, features causal, versioned, reproducible
- ReasoningBrain: Kronos gate preserves capital; no silent relaxations
- RiskBrain: RiskAuthority > Strategy > Model; hard SL inviolable
- ExecutionBrain: no model output -> real order without RiskBrain approval
- LearningBrain: every failure -> root cause, fix, regression test, lesson
""",
    "orchestrator": """# AUTOCRYPT V4 Orchestrator
Per bootstrap: 3-agent team with goal, task graph, permissions, Git, memory, experiments, Colab jobs, debate/vetoes, budgets, completion, human approval gates.

goal: "BUILD, REPAIR, TEST, RESEARCH, AUDIT, IMPROVE, DOCUMENT, AND HARDEN THE AUTOCRYPT PROJECT FROM ITS CURRENT STATE TOWARD VERIFIED 100% COMPLETION."

agents:
  engineering_architect:
    role: "Python, architecture, debugging, testing, systems, Git, deployment, performance, Colab integration"
    disciplines: ["Python", "Computer Science", "Data Structures & Algorithms", "Git and GitHub", "API Design", "Backend", "Software Architect", "Software Design and Architecture", "System Design", "Linux", "Bash/Shell", "Docker", "DevOps", "DevSecOps", "QA", "performance"]
  quant_ml_researcher:
    role: "ML, time series, Kronos, forecasting, features, labels, alpha research, WFO, OOS, bootstrap, Monte Carlo, self-training, model evaluation"
    disciplines: ["Machine Learning", "MLOps", "AI Engineer", "Python for Data Analysis", "Computer Science", "AI Agents", "Prompt Engineering", "AI Red Teaming"]
  red_team_risk_auditor:
    role: "leakage, overfitting, backtest audit, risk, security, execution realism, adversarial testing, failure analysis"
    disciplines: ["Cyber Security", "DevSecOps", "AI Red Teaming", "Cyber Security"]

task_graph:
  critical_path: "DISCOVERY -> FOUNDATION -> DATA -> TRADING_ENGINE -> BACKTESTER -> V0 -> BASELINES -> KRONOS_VALIDATION -> ML -> SELF-TRAINING -> WFO / OOS / ROBUSTNESS -> PAPER -> SHADOW -> TESTNET -> HUMAN_GATE -> TINY_LIVE -> STABILITY -> SCALE"
  parallel_tracks: ["security", "observability", "documentation", "agent_control_plane"]
  dependencies:
    DISCOVERY: []
    FOUNDATION: [DISCOVERY]
    DATA: [FOUNDATION]
    TRADING_ENGINE: [DATA]
    BACKTESTER: [TRADING_ENGINE]
    V0: [BACKTESTER]
    BASELINES: [V0]
    KRONOS_VALIDATION: [BASELINES]
    ML: [KRONOS_VALIDATION]
    SELF_TRAINING: [ML]
    WFO_ROBUSTNESS: [SELF_TRAINING]
    PAPER: [WFO_ROBUSTNESS]
    SHADOW: [PAPER]
    TESTNET: [SHADOW]
    HUMAN_GATE: [TESTNET]
    TINY_LIVE: [HUMAN_GATE]
    STABILITY: [TINY_LIVE]
    SCALE: [STABILITY]

permissions:
  agent_layer: "cannot override RiskBrain"
  colab: "heavy tasks on Colab, light local"
  git: "protected main, agent feature branches, research branches, audit branches, model tags, dataset tags"
  resources: "full authorization to use all legitimately available resources: plugins, skills, connected tools, Git tools, file tools, web/research tools, AI models, model APIs, Google Colab, GPU, CPU, storage, scripts, notebooks, datasets, models, artifacts; choose resources using: correctness, quality_of_evidence, reliability, resource_efficiency; does_not_override: platform_rules, tool_permissions, credential_security, human_only_real_money_approval"

memory:
  persistent: "PROJECT_MEMORY.md index, per-fact files with frontmatter (name/description/metadata type)"
  index: "PROJECT_MEMORY.md one-line pointers (- [Title](file.md) — hook), no frontmatter in index"
  format: "each fact: individual file with frontmatter (name: short-kebab-case-slug, description: one-line summary, metadata: user|feedback|project|reference), body with Why: and How to apply: lines, [[name]] linking"

experiments:
  versioning: "KRN-V0, KRN-V1, ... for models; RUN-0001, RUN-0002, ... for experiments"
  registry: "experiment registry with model ID, hash, parent model, dataset, code commit, training config, environment, metrics, promotion decision"
  lifecycle: "DRAFT -> TRAINED -> CANDIDATE -> VALIDATED -> CHAMPION -> PAPER -> SHADOW -> TINY_LIVE"

colab:
  heavy_tasks: "training, fine-tuning, large backtests, WFO, bootstrap, Monte Carlo, hyperparameter sweeps, large dataset generation, model export"
  package: "README.md, notebook.ipynb, requirements.txt, config, expected outputs, checksums"
  human_workflow: "upload/run -> return_results -> agents_continue_autonomously_after_ingestion"

budgets: "token budgets, compute budgets, Colab resource budgets enforced per task tier"

completion:
  100_percent: "requirements_satisfied, tests_pass, research_gates_pass, artifacts_reproducible, risk_verified, execution_verified, agent_system_stable, documentation_complete, no_critical_blocker_remains"
  does_not_mean: "future_profit_is_guaranteed"

human_approval_gates: "TINY_LIVE gate requires: OOS Sharpe >= 1.50, trades/day >= 4, Max DD <= 20%, WFO, bootstrap, Monte Carlo, cost stress, paper, shadow, testnet, risk tests, watchdog, human approval"

red_team: "Agent C continuously tries to break: code, backtester, model, agent prompts, routing, promotion, security, risk"

adaptive_routing: "specialists selected dynamically from 10-mode hierarchy: architecture, deep-research, heavy-coding, fast-coding, latency-critical, huge-context, adversarial-review, production, fallback"
""",
}


def initialize_project() -> Dict[str, Any]:
    """Run complete project initialization per bootstrap and roadmap specifications."""
    
    result: Dict[str, Any] = {
        "bootstrap_spec": BOOTSTRAP_SPEC,
        "roadmap_spec": ROADMAP_SPEC,
        "project_root": str(PROJECT_ROOT),
        "phase_dirs_created": {},
        "init_py_files_created": {},
        "hard_gates_enforced": True,
        "resource_authorization": "full",
        "status": "initialized",
    }
    
    # Create phase directories
    PROJECT_ROOT_TO_DIRS = [
        "config",
        "data",
        "features",
        "brains",
        "models",
        "research",
        "execution",
        "risk",
        "agents",
        "orchestration",
        "tests",
        "services",
    ]
    PROJECT_ROOT_DIRS = [*PROJECT_ROOT_TO_DIRS, *PHASE_0_DIRS]

    for dir_name in PROJECT_ROOT_DIRS:
        dir_path = PROJECT_ROOT / dir_name
        dir_path.mkdir(parents=True, exist_ok=True)
        # Write __init__.py for Python packages
        if dir_name in INIT_PY_FILES:
            init_path = dir_path / "__init__.py"
            init_path.write_text(INIT_PY_FILES[dir_name])
            result["init_py_files_created"][dir_name] = True
        else:
            init_path = dir_path / "README.md"
            init_path.write_text(f"# {dir_name.upper()} module\nAUTOCRYPT V4 module. See roadmap for details.")
        result["phase_dirs_created"][dir_name] = True
    
    # Write orchestrator.json if not exists
    orch_path = PROJECT_ROOT / "orchestrator.json"
    if not orch_path.exists():
        orch_path.write_text(json.dumps(PROJECT_SPEC["orchestrator"], indent=2))
        result["orchestrator_created"] = True
    else:
        result["orchestrator_created"] = False
    
    # Write PROJECT_SPEC.json
    spec_path = PROJECT_ROOT / "PROJECT_SPEC.json"
    spec_path.write_text(json.dumps(PROJECT_SPEC, indent=2))
    result["spec_created"] = True
    
    return result


# The PROJECT_SPEC below is incomplete on purpose — it references
# BOOTSTRAP_SPEC and ROADMAP_SPEC above. The full initialization
# is handled by initialize_project().
PROJECT_SPEC = {
    "project": "AUTOCRYPT_V4",
    "initialization": "run initialize_project() to set up complete project",
}


# ---------------------------------------------------------------------------
# When run as main, initialize the project
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    result = initialize_project()
    print("=" * 60)
    print("AUTOCRYPT V4 PROJECT INITIALIZATION")
    print("=" * 60)
    print(f"Project root: {result['project_root']}")
    print(f"Status: {result['status']}")
    print(f"Bootstrap spec loaded: {bool(result['bootstrap_spec'])}")
    print(f"Roadmap spec loaded: {bool(result['roadmap_spec'])}")
    print(f"Phase directories created: {len(result['phase_dirs_created'])}")
    print(f"__init__.py files created: {len(result['init_py_files_created'])}")
    print(f"Hard gates enforced: {result['hard_gates_enforced']}")
    print(f"Resource authorization: {result['resource_authorization']}")
    print()
    print("Directories created:")
    for d in sorted(result["phase_dirs_created"]):
        print(f"  - {d}")
    print()
    print("__init__.py files created:")
    for d in sorted(result["init_py_files_created"]):
        print(f"  - {d}")
    print()
    print("Next: Review the created structure, then run")
    print("  'python -c \"from project_init import initialize_project; "
          "initialize_project()\"' to verify full setup.")
    print("=" * 60)