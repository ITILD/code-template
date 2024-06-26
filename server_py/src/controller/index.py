# self
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from config.log import console
from config.fastapi_config import app
from service.index import TableService
# lib
from fastapi import APIRouter, status
from config.path import path_html

# 配置静态文件服务
app.mount("/", StaticFiles(directory=path_html, html=True), name="static")
# 首页 app非router挂载
# @app.get("/", response_class=HTMLResponse)
# async def server():
#     console.log('初始首页html')
#     html_file = open("index.html", 'r').read()
#     return html_file

# 基础db
router = APIRouter()
# 测试
@router.get("/create",status_code=status.HTTP_201_CREATED)
async def create():
    '''创建未创建的表'''
    console.log('test1')
    result=await TableService.create()
    return result

app.include_router(router,prefix="/db",tags=['db'])
console.log('...controller index')
