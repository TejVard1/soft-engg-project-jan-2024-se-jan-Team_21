# Online Support Ticket Application
# Tushar Supe : 21f1003637
# Vaidehi Agarwal: 21f1003880
# File Info: Contains fixtures for testing.

# --------------------  Imports  --------------------

from application import create_app
import pytest
from application.logger import logger

# --------------------  Constants  --------------------

# Please set following required constants to mimic a specific user role.

# STUDENT
student_user_id = "edda661776886520e981857f5f8d61d6"
student_web_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InN0MUBnbWFpbC5jb20iLCJleHBpcnkiOjE3MTIxNjY0NTV9.ynPeXeOZlUaaPrMW6PkS4UlVb7O-46BFu-1Li89a8PY"
 
# SUPPORT
support_user_id = "2827867f2ab1f641dc28a3486f9b8045"
support_web_token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InN1MUBnbWFpbC5jb20iLCJleHBpcnkiOjE3MTIxNjY4NTV9.lCTYmv7FuuHt1hVOOI8pv5v1azf8HWIqR1i4W8Wh804"

# ADMIN
admin_user_id = "c69c58b0ecf745b8cf1a3dd80cead97f"
admin_web_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IjEyMTB0ZWpAZ21haWwuY29tIiwiZXhwaXJ5IjoxNzEyMTY2OTQ1fQ.ACmdwbgeRHpLOvDlitkvA_jmNMn-Y5q-sZjJS0X6m5k"

# --------------------  Code  --------------------

# before testing set current dir to `\code\backend`
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(env_type="test")
    logger.info("Testing fixture set.")
    
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!