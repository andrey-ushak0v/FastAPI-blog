from fastapi import APIRouter, UploadFile, File, Depends, BackgroundTasks
from models.auth import User
from services.auth import get_current_user
from services.reports import ReportServce
from fastapi.responses import StreamingResponse


router = APIRouter(
    prefix='/reports'
)


@router.post('/import')
def import_csv(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    reports_service: ReportServce = Depends(),
        ):
    background_tasks.add_task(
        reports_service.import_csv,
        user.id,
        file.file,
    )


@router.get('/export')
def export_csv(
    user: User = Depends(get_current_user),
    reports_service: ReportServce = Depends(),
):
    report = reports_service.export_csv(user.id)
    return StreamingResponse(
        report,
        media_type='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=report.csv'
        }
    )
