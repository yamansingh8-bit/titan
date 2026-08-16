# AUTOCRYPT V4 — Data Engineering
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
