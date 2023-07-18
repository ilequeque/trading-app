from fastapi import APIRouter, Depends
from starlette.background import BackgroundTasks

from src.auth.base_config import current_user
from src.tasks.tasks import send_email_report_dashboard

router = APIRouter(prefix='/report')


@router.get('/dashboard')
def get_dashboard_report(user=Depends(current_user)):
    # background_tasks.add_task(send_email_report_dashboard, user.username)
    send_email_report_dashboard.delay(user.username)
    return {
        "status": 200,
        "data": "Email has been sent",
        "details": None
    }
