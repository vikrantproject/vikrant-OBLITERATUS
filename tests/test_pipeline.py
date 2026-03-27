"""Tests for abliteration pipeline."""

def test_pipeline_import():
    from vikrant_obl.pipeline import VikrantAbliterationPipeline
    assert VikrantAbliterationPipeline is not None

def test_pipeline_init():
    from vikrant_obl.pipeline import VikrantAbliterationPipeline
    pipeline = VikrantAbliterationPipeline("test-model")
    assert pipeline.model_name == "test-model"
    assert pipeline.method == "svd_normpres"
