from statistics import mean

from fastapi import FastAPI
from nicegui import ui


app = FastAPI(title="Average Calculator API")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


def parse_and_average(raw: str | None) -> str:
    raw = raw or ""
    tokens = [t for part in raw.split(",") for t in part.strip().split()] if raw else []
    
    # Handle empty input
    if not tokens:
        return "Error: no values provided"
    
    # Handle non-numeric input
    try:
        values = [float(t) for t in tokens if t]
    except ValueError:
        return "Error: non-numeric value detected"
    
    # Handle case where all tokens were invalid/empty
    if not values:
        return "Error: no valid numeric values"
        
    return f"Average: {mean(values):.4f}"


@ui.page("/")
def home() -> None:
    ui.label("CSE120 GitHub Workshop").classes("text-2xl font-bold")
    ui.label("Average Calculator").classes("text-lg text-gray-600 mb-4")
    numbers_input = ui.textarea(label="Numbers (comma or space separated)").classes("w-full h-32")
    result_label = ui.label("Enter numbers and click Compute").classes("mt-4 text-lg")

    def compute() -> None:
        result_label.text = parse_and_average(numbers_input.value)

    ui.button("Compute Average", on_click=compute).classes("mt-2")
    ui.separator()


# Bind NiceGUI to FastAPI app so both share the same server process.
ui.run_with(app)
