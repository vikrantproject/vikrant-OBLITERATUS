# Folder Structure

vikrant-OBLITERATUS/
├── .github/
│   └── workflows/
│       ├── ci.yml                    # Continuous Integration
│       ├── publish.yml               # PyPI publishing
│       └── hf_sync.yml               # HuggingFace Space sync
├── vikrant_obl/                      # Main package
│   ├── __init__.py                   # Package initialization
│   ├── cli.py                        # CLI entry point (vobl command)
│   ├── pipeline.py                   # Main abliteration pipeline
│   ├── stages/                       # 8 pipeline stages
│   │   ├── __init__.py
│   │   ├── initialize.py             # Stage 1: INITIALIZE
│   │   ├── acquire.py                # Stage 2: ACQUIRE
│   │   ├── instrument.py             # Stage 3: INSTRUMENT
│   │   ├── probe.py                  # Stage 4: PROBE
│   │   ├── decompose.py              # Stage 5: DECOMPOSE
│   │   ├── intervene.py              # Stage 6: INTERVENE
│   │   ├── validate.py               # Stage 7: VALIDATE
│   │   └── publish.py                # Stage 8: PUBLISH
│   ├── methods/                      # 10 abliteration methods
│   │   ├── __init__.py
│   │   ├── baseline_diffmeans.py
│   │   ├── svd_normpres.py          # Default recommended
│   │   ├── svd_iterative.py
│   │   ├── expert_granular.py
│   │   ├── bayesian_cot.py
│   │   ├── semantic_inversion.py
│   │   ├── maximum_entropy.py
│   │   ├── adaptive_finetune.py     # NEW
│   │   ├── cross_lingual.py         # NEW
│   │   └── quantized_aware.py       # NEW
│   ├── analysis/                     # 20 analysis modules
│   │   ├── __init__.py
│   │   ├── layer_alignment.py
│   │   ├── logit_lens.py
│   │   ├── whitened_svd.py
│   │   ├── activation_probe.py
│   │   ├── ouroboros_detector.py
│   │   ├── concept_cone.py
│   │   ├── alignment_fingerprint.py
│   │   ├── multi_token_position.py
│   │   ├── sparse_surgeon.py
│   │   ├── causal_tracing.py
│   │   ├── residual_stream.py
│   │   ├── linear_classifier.py
│   │   ├── universality.py
│   │   ├── steering_vectors.py
│   │   ├── evaluator.py
│   │   ├── finetune_impact.py       # NEW
│   │   ├── voice_refusal.py         # NEW
│   │   ├── session_diff.py          # NEW
│   │   ├── provenance_tracker.py    # NEW
│   │   └── dashboard_report.py      # NEW
│   ├── features/                     # 4 revolutionary features
│   │   ├── __init__.py
│   │   ├── auto_finetune.py         # Feature A
│   │   ├── scanner.py               # Feature B: Dark Web Scanner
│   │   ├── collaboration.py         # Feature C: Real-time collab
│   │   └── voice.py                 # Feature D: Voice/audio support
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── app.py                   # Gradio app (12 tabs)
│   │   └── tabs/
│   │       ├── dashboard.py
│   │       ├── obliterate.py
│   │       ├── finetune.py
│   │       ├── scanner.py
│   │       ├── collaborate.py
│   │       ├── voice.py
│   │       ├── analysis.py
│   │       ├── benchmark.py
│   │       ├── compare.py
│   │       ├── report.py
│   │       ├── leaderboard.py
│   │       └── docs.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   └── presets.py               # 116 model presets
│   ├── telemetry/
│   │   ├── __init__.py
│   │   └── community.py
│   └── py.typed                      # Type hints marker
├── tests/                            # Test suite (1000+ tests)
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_pipeline.py
│   ├── test_stages.py
│   ├── test_methods.py
│   ├── test_analysis.py
│   ├── test_features.py
│   └── test_ui.py
├── examples/                         # Example configs
│   ├── basic_abliteration.yaml
│   ├── with_finetune.yaml
│   ├── voice_abliteration.yaml
│   └── collaborative_session.yaml
├── notebooks/
│   └── vikrant_obl.ipynb            # Google Colab notebook
├── docs/
│   ├── index.md
│   ├── api_reference.md
│   ├── tutorials/
│   └── research/
├── paper/                            # LaTeX research paper
│   ├── main.tex
│   ├── appendix.tex
│   └── references.bib
├── pyproject.toml                    # Package configuration
├── requirements.txt                  # Core dependencies
├── README.md                         # Main documentation
├── LICENSE                           # AGPL-3.0
├── SECURITY.md                       # Security policy
├── CONTRIBUTING.md                   # Contribution guidelines
└── .gitignore
