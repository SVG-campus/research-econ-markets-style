from methodology_preamble import assert_run_card, build_run_card, init_notebook, load_smoke_caps


def test_load_smoke():
    c = load_smoke_caps()
    assert c["pillar"] == "research-econ-markets-style"
    assert "methodology_caps" in c


def test_init_notebook():
    info = init_notebook()
    assert info["seed"] == 42
    assert info["pillar"] == "research-econ-markets-style"


def test_run_card_roundtrip():
    info = init_notebook()
    rc = build_run_card(
        run_id="pytest_smoke",
        hypothesis="test",
        metric="m",
        null="none",
        truth_scope="unit test",
        seed=info["seed"],
    )
    assert_run_card(rc)
