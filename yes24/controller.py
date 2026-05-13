from fastapi import APIRouter
from service import craw

router=APIRouter(prefix='/books')

@router.get('/stats')
async def item():
    return craw()