from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    BackgroundTasks
)
from fastapi.responses import StreamingResponse

from workshop.services.auth import get_current_user
from workshop.models.auth import User
from workshop.services.reports import ReportsService

router = APIRouter(
    prefix='/reports',
    tags = ['reposrts'],
)


@router.post('/import')
def import_csv(
    backgrounds_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    reports_service: ReportsService = Depends(),
):
    backgrounds_tasks.add_task(
        reports_service.import_csv,
        user.id,
        file.file
    )


@router.get('/export')
def export_csv(
    user: User = Depends(get_current_user),
    reports_service: ReportsService = Depends(),
):
    report = reports_service.export_csv(user.id)
    return StreamingResponse(
        report,
        media_type='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=reports.csv'
        },

    )