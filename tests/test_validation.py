def validate_job_title(title):
    if not title or title.strip() == "":
        return False
    return True

def test_validate_job_title():
    assert validate_job_title("QA Engineer") == True
    assert validate_job_title("") == False
    assert validate_job_title("   ") == False
