from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ai.education import (
    answer_question,
    explain_concept,
    generate_quiz,
    summarize_text,
    learning_recommendation,
)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "answer": ""
        }
    )


@app.post("/", response_class=HTMLResponse)
async def chatbot(
    request: Request,
    task: str = Form(...),
    question: str = Form(...)
):

    if task == "question":
        answer = answer_question(question)

    elif task == "explain":
        answer = explain_concept(question)

    elif task == "quiz":
        answer = generate_quiz(question)

    elif task == "summary":
        answer = summarize_text(question)

    elif task == "recommend":
        answer = learning_recommendation(question)

    else:
        answer = "Invalid task."

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "answer": answer
        }
    )