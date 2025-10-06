# ruff: noqa: I001  # Allow simple two-line import order without enforced resorting
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_index_page_renders():
    """Ensure the NiceGUI root page renders and contains expected labels.

    We don't execute JS or interact with UI components here; we just verify
    that the static HTML delivered includes the workshop title and subtitle.
    """
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.text
    assert "CSE120 GitHub Workshop" in body
    assert "Average Calculator" in body
    # Confirm the compute button label present
    assert "Compute Average" in body