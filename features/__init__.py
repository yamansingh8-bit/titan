"""AUTOCRYPT V4 — Features Engineering

Per roadmap Phase 15: Alpha stack L0-L15, feature families causal, versioned and reproducible.
"""

# Alpha stack L0-L15 (per roadmap Phase 15)
ALPHA_STACK = {
    "L0": "Infrastructure / Data / Audit",
    "L1": "Classical indicators",
    "L2": "Regime",
    "L3": "Relative value",
    "L4": "Crypto carry",
    "L5": "Stat-arb",
    "L6": "Microstructure",
    "L7": "Liquidation",
    "L8": "Volatility",
    "L9": "ML fusion",
    "L10": "Meta-labeling",
    "L11": "Portfolio",
    "L12": "Execution",
    "L13": "Risk",
    "L14": "Learning",
    "L15": "Optional reasoning/research",
}

# Feature families (per roadmap Phase 15)
FEATURE_FAMILIES = {
    "L1_classical": {
        "names": ["EMA", "RSI", "ATR", "Bollinger", "Donchian", "ADX"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L2_regime": {
        "names": ["regime"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
        "one_system_wide_classifier": True,  # L2: strict ONE system-wide classifier; no downstream module computes its own regime
    },
    "L3_relative_value": {
        "names": ["cointegration", "spreads", "z_score"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L4_crypto_carry": {
        "names": ["funding", "basis", "carry"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L5_stat_arb": {
        "names": ["cross-sectional_momentum", "mean_reversion"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L6_microstructure": {
        "names": ["OFI", "CVD", "book_imbalance"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L7_liquidation": {
        "names": ["liquidation_intensity", "OI_shock"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L8_volatility": {
        "names": ["realized_volatility", "compression", "expansion"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L9_ml_fusion": {
        "names": ["ML_fusion"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L10_meta_labeling": {
        "names": ["meta_labeling"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L11_portfolio": {
        "names": ["portfolio"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L12_execution": {
        "names": ["execution"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L13_risk": {
        "names": ["risk"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L14_learning": {
        "names": ["learning"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
    "L15_optional_reasoning": {
        "names": ["optional_reasoning"],
        "causal": True,
        "versioned": True,
        "reproducible": True,
    },
}

# Baseline ladder (per roadmap Phase 13)
BASELINE_LADDER = {
    "B0": "strategy_only",
    "B1": "strategy + classical_ML",
    "B2": "strategy + evolved_Kronos",
    "B3": "strategy + ML + evolved_Kronos",
    "B4": "strategy + ML + meta_label",
    "B5": "complete_candidate",
    "question": "Which_component_actually_adds_durable_value?",
}

# Evolved Kronos (per roadmap Phase 14)
EVOLVED_KRONOS = {
    "pipeline": "OHLCV → causal_rolling_context → evolved_Kronos → forecast / signal / confidence → trading_decision",
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

# Machine learning baselines (per roadmap Phase 18)
ML_BASELINES = {
    "B0": "strategy_only",
    "B1": "strategy + classical_ML",
    "baselines": ["Logistic_Regression", "Random_Forest", "LightGBM", "XGBoost"],
    "then": "evaluate_deeper_models_only_when_justified",
}

# Label engineering (per roadmap Phase 15)
LABEL_ENGINEERING = {
    "avoid": "final_relaince_on_profit_0_is_yes",
    "structured_targets": ["direction", "TAKE/REJECT", "future_return", "MFE", "MAE", "TP_hit", "SL_hit", "time_to_exit"],
    "preferred_design": "triple_barrier_labeling",
}

# Meta-labeling (per roadmap Phase 16)
META_LABELING = {
    "core_idea": "strategy_proposes_candidate → meta_model_decides_TAKE / REJECT",
    "possible_outputs": ["P(short)", "P(flat)", "P(long)"],
    "constraint": "meta_model_must_not_become_uncontrolled_hidden_strategy_generator",
}

# Self-training (per roadmap Phase 17)
SELF_TRAINING = {
    "core_loop": "CHAMPION → market_outcomes → training_dataset → candidate_training → candidate_model → OOS_WFO → red_team → promotion_gate",
    "options": ["reject", "accept → new_champion"],
    "never": "repeatedly_optimize_on_the_same_locked_holdout",
}

# MLOps (per roadmap Phase 19)
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
    "lifecycle": "DRAFT → TRAINED → CANDIDATE → VALIDATED → CHAMPION → PAPER → SHADOW → TINY_LIVE",
}

# WFO + OOS (per roadmap Phase 20)
WFO_OOS = {
    "required_folds": ["fold_1", "fold_2", "fold_3", "fold_4+"],
    "track": ["Sharpe", "Sortino", "Max_DD", "Profit_Factor", "Expectancy", "Win_Rate", "Trade_count", "Return", "Cost-adjusted_return"],
    "one_lucky_fold_cannot_promote": True,
}

# Robustness (per roadmap Phase 21)
ROBUSTNESS = {
    "required": ["bootstrap", "Monte_Carlo", "parameter_dispersion", "cost_stress"],
    "cost_stress": ["1.0x", "1.5x", "2.0x"],
    "model_should_remain_defensible": True,
}

# Goal optimization (per roadmap Phase 22)
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

# Risk / Portfolio (per roadmap Phase 23)
RISK_PORTFOLIO = {
    "hard_boundaries": ["hard_SL = 1.5%", "portfolio_DD_circuit_breaker = 5%", "max_active_positions = 3"],
    "authority": "RiskBrain > Strategy > Model",
    "self_training_cannot": "silently_rewrite_risk_policy",
}

# Execution (per roadmap Phase 24)
EXECUTION = {
    "test": ["order_creation", "reduce_only", "SL", "TP", "partial_fills", "cancel", "reconnect", "position_reconciliation", "stale_data_handling", "latency"],
    "no_direct_become": "real_money_order_without_RiskBrain_approval",
}

# Observability (per roadmap Phase 25)
OBSERVABILITY = {
    "required": ["structured_logs", "health_checks", "model_health", "data_health", "WebSocket_health", "REST_health", "execution_latency", "RAM", "CPU", "GPU_job_state", "position_state", "risk_state"],
}

# AI Agent System (per roadmap Phase 26)
AGENT_SYSTEM = {
    "recommended_hierarchy": ["Fable_5", "GPT-5.6_Sol", "adaptive_specialist_pool", "verification", "red-team", "final_audit"],
    "permanent_AutoCrypt_capabilities": [
        "Engineering_Architect",
        "Quant_ML_Researcher",
        "Red_Team_Risk_Auditor",
    ],
    "specialists_selected_dynamically": True,
    "minimum_models_required_for_correctness": True,
    "full_hierarchy_when_justified": True,
}

# Agent Memory + Experiment Memory (per roadmap Phase 27)
AGENT_MEMORY = {
    "store": ["goals", "decisions", "failures", "discoveries", "assumptions", "experiments", "datasets", "models", "lessons"],
    "every_important_failure_becomes": "root_cause, fix, regression_test, lesson",
}

# Adaptive Model Routing (per roadmap Phase 28)
ADAPTIVE_ROUTING = {
    "use_models_based_on_task_type": True,
    "not_popularity": True,
    "architecture → architecture_specialist": True,
    "deep_research → research_specialist": True,
    "heavy_coding → principal_coding_specialist": True,
    "autonomous_coding → autonomous_coding_specialist": True,
    "routine_coding → fast_coding_specialist": True,
    "latency_critical → latency_critical_specialist": True,
    "adversarial_review → red_team_specialist": True,
    "production → production_specialist": True,
    "fallback → backup_specialist": True,
    "minimum_models_required_for_correctness": True,
    "full_hierarchy_when_complexity_or_risk_justifies_it": True,
}

# Source-first execution (per roadmap Phase 28)
SOURCE_FIRST_EXECUTION = {
    "context_first": True,
    "execute": True,
    "validate": True,
    "final_source_filter": True,
    "output": True,
    "before_work": "read_relevant_project_files, understand_current_state, understand_constraints, check_previous_failures",
    "after_work": "re_check_source_consistency, remove_unsupported_assumptions, confirm_metrics, confirm_architecture",
}

# Full resource authorization (per roadmap Phase 30-34)
FULL_RESOURCE_AUTHORIZATION = {
    "agents": "may_use_all_legitimately_available_resources_within_project_scope",
    "resources": ["plugins", "skills", "connected_tools", "git_tools", "file_tools", "web_research_tools", "ai_models", "model_apis", "google_colab", "gpu", "cpu", "storage", "scripts", "notebooks", "datasets", "models", "artifacts"],
    "choose_resources_using": ["correctness", "quality_of_evidence", "reliability", "resource_efficiency"],
    "does_not_override": "platform_rules, tool_permissions, credential_security, human_only_real_money_approval",
}

# Colab-first research (per roadmap Phase 30-31)
COLAB_FIRST_RESEARCH = {
    "heavy_tasks": ["training", "fine_tuning", "large_backtests", "WFO", "bootstrap", "Monte_Carlo", "hyperparameter_sweeps", "large_dataset_generation", "model_export"],
    "package": ["README.md", "notebook.ipynb", "requirements.txt", "config", "expected_outputs", "checksums"],
    "human_workflow": "upload/run → return_results → agents_continue_autonomously_after_ingestion",
}

# Paper trading (per roadmap Phase 32)
PAPER_TRADING = {
    "before_real_money": "historical_OOS → paper",
    "track": ["signals", "latency", "slippage", "expected_vs_actual_PnL", "missed_trades", "execution_failures", "risk_vetoes"],
}

# Shadow mode (per roadmap Phase 33)
SHADOW_MODE = {
    "use_live_data": "without_real_capital",
    "compare": ["model_decision", "expected_execution", "simulated_fill", "market_behavior"],
}

# Testnet (per roadmap Phase 34)
TESTNET = {
    "validate": ["order_create", "cancel", "reduce_only", "SL", "TP", "partial_fills", "reconnect", "position_reconciliation", "emergency_halt"],
    "no_live_capital": "before_this_gate",
}

# Tiny live gate (per roadmap Phase 35)
TINY_LIVE_GATE = {
    "must_pass": ["OOS_Sharpe >= 1.50", "trades_per_day >= 4", "Max_DD <= 20%"],
    "also_pass": ["WFO", "bootstrap", "Monte_Carlo", "cost_stress", "paper", "shadow", "testnet", "risk_tests", "watchdog", "human_approval"],
    "then": "TINY_LIVE",
}

# Scale (per roadmap Phase 36)
SCALE = {
    "separate_gate": True,
    "evaluate": ["live_stability", "paper_live_divergence", "slippage", "latency", "risk", "model_drift"],
    "no_automatic_capital_scaling": True,
}

# Continuous learning (per roadmap Phase 37)
CONTINUOUS_LEARNING = {
    "once_stable": "live/paper_outcomes → dataset_update → challenger → OOS_WFO → red_team → promotion",
    "live_outcomes_cannot": "rewrite_evaluation_protocol_silently",
}

# Drift detection (per roadmap Phase 38)
DRIFT_DETECTION = {
    "monitor": ["feature_drift", "regime_drift", "performance_drift", "trade_frequency_drift", "confidence_drift", "execution_drift", "cost_drift"],
    "trigger": "research_review_when_production_diverges_materially_from_validated_behavior",
}

# Model demotion (per roadmap Phase 39)
MODEL_DEMOTION = {
    "champion_can_be_demoted": True,
    "when": ["new_evidence_invalidates_it", "live_performance_degrades", "data_pipeline_changes", "model_corruption_occurs", "risk_assumptions_change"],
    "fallback": "previous_validated_champion",
}

# Security hardening (per roadmap Phase 40)
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

# Documentation (per roadmap Phase 41)
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

# 100% completion system (per roadmap Phase 41-42)
COMPLETION_100 = {
    "means": "requirements_satisfied, tests_pass, research_gates_pass, artifacts_reproducible, risk_verified, execution_verified, agent_system_stable, documentation_complete, no_critical_blocker_remains",
    "does_not_mean": "future_profit_is_guaranteed",
}

# Master checklist (per roadmap Phase 47)
MASTER_CHECKLIST = {
    "foundation": ["discovery", "repository_health", "Python_architecture", "Git_workflow", "API/CLI_boundaries", "state_machine"],
    "data": ["real_Binance_data", "validation", "manifests", "feature_pipeline", "label_pipeline"],
    "trading": ["strategy", "risk", "portfolio", "execution", "backtester"],
    "ml": ["classical_ML_baseline", "evolved_Kronos", "meta_model", "meta_label", "training_pipeline", "self_training"],
    "validation": ["causality", "leakage", "WFO", "OOS", "immutable_holdout", "bootstrap", "Monte_Carlo", "cost_stress"],
    "agents": ["orchestrator", "engineering_agent", "quant_ML_agent", "adaptive_routing", "shared_memory", "Git_isolation", "evidence_system", "voting", "veto", "no_progress", "completion_checker"],
    "deployment": ["paper", "shadow", "testnet", "human_live_gate", "monitoring", "watchdog", "emergency_halt"],
}

# Golden rule (per roadmap Phase 50)
GOLDEN_RULE = "Learn only what improves the project. Build only what the project can verify. Promote only what survives independent evaluation."

# Source basis (Per roadmap Phase 51)
SOURCE_BASIS = "nilbuild/developer-roadmap repository as external taxonomy, mapped into AUTOCRYPT project architecture, evolved-Kronos/self-training plan, multi-agent design, and source-first operating protocol."

# Phase 0 (Discovery) reference
PHASE_0 = "DISCOVERY"

# Phase 1 reference
PHASE_1 = "PYTHON_ENGINEERING"