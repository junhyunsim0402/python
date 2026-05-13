# [1] 라우터
from fastapi import APIRouter

# APIRouter(prefix='/공통도메인')
# vs @RequestMapping('/공통도메인')
router=APIRouter(prefix='/api')

# [3] 서비스 불러오기
from service import item_service

# [2] REST API 정의
# (1) GET
@router.get('/item')
async def item(id:int):
    return item_service.item(id)

# (2) GET
@router.get('/items')
async def items():
    return item_service.items()

# (3) POST
@router.post('/save')
async def save(item:dict):
    return item_service.save(item)

# (3) PUT
@router.put('/update')
async def update(item:dict):
    return item_service.update(item)

# (3) DELETE
@router.delete('/delete')
async def delete(id:int):
    return item_service.delete(id)
