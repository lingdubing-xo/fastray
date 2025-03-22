from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
from config import settings

templates = Jinja2Templates(directory=settings.template_dir)

router = APIRouter()

@router.get("/index", summary="首页")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": settings.project_name,
            "description": "一个高效、安全、智能的电动车管理平台"
        }
    )
