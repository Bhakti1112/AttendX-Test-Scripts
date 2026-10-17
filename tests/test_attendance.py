
import unittest


def mark_attendance(student_id, status):
    """Sample attendance-marking logic for AttendX."""
    if not student_id:
        return False

    if status not in ("Present", "Absent"):
        return False

    return True


class TestAttendance(unittest.TestCase):

    def test_mark_present(self):
        self.assertTrue(mark_attendance("STU001", "Present"))

    def test_mark_absent(self):
        self.assertTrue(mark_attendance("STU002", "Absent"))

    def test_missing_student_id(self):
        self.assertFalse(mark_attendance("", "Present"))

    def test_invalid_status(self):
        self.assertFalse(mark_attendance("STU001", "Late"))


if __name__ == "__main__":
    unittest.main()