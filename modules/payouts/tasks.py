import time
import logging
from celery import shared_task
from .models import Payout, PayoutStatus

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def process_payout_task(self, payout_id):
    try:
        payout = Payout.objects.get(id=payout_id)
        logger.info(f"Начало обработки выплаты {payout.id}")

        # Меняем статус на processing
        payout.status = PayoutStatus.PROCESSING
        payout.save(update_fields=["status"])

        time.sleep(5)

        if payout.amount > 1000:
            payout.status = PayoutStatus.COMPLETED
        else:
            payout.status = PayoutStatus.FAILED

        payout.save(update_fields=["status"])
        logger.info(f"Выплата {payout.id} завершена со статусом {payout.status}")

    except Payout.DoesNotExist:
        logger.error(f"Платёж с id {payout_id} не найден")
