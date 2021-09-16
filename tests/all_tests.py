from mock_logging_service import LoggingService
from mock_db_service import MockDb

# logger = LoggingService()
# logger.log_info("test 1")
# logger.log_info("test 2")
# logger.log_error("error 1")
# logger.log_error("error 2")
# print(logger.get_all_logs())

db = MockDb()
preference = {
    'user': 'jon'
}
db.add_preference(preference)

print(db.get_preferences('jim'))
