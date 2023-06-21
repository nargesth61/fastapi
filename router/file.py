from fastapi import FastAPI,status,Response,APIRouter ,File
from fastapi.responses import FileResponse


router = APIRouter(prefix='/file', tags=['file'])

@router.post('/file')
def get_file(file:bytes=File(...)):
    data = file.decode('utf-8')
    return {
        'data':data
    }


@router.post('/download/{name}',response_class=FileResponse)
def download_file(name:str):
    path=f'test/{name}'
    return path