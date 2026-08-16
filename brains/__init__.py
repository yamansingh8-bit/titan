# AUTOCRYPT V4 — 5-Brain Architecture
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
