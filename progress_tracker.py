import json
import os
from datetime import datetime

class ProgressTracker:
    def __init__(self):
        self.progress_file = "trading_academy/user_progress.json"

    def get_user_stats(self, user_id):
        """Get user's learning statistics"""
        try:
            if os.path.exists(self.progress_file):
                with open(self.progress_file, 'r') as f:
                    progress_data = json.load(f)

                user_data = progress_data.get(str(user_id), {})

                # Calculate statistics
                total_lessons = sum(len(course.get('completed_lessons', [])) for course in user_data.values())
                total_courses = len([course for course in user_data.values() if course.get('completed', False)])

                # Calculate average quiz score
                all_scores = []
                for course in user_data.values():
                    quiz_scores = course.get('quiz_scores', {})
                    all_scores.extend(quiz_scores.values())

                avg_score = sum(all_scores) / len(all_scores) if all_scores else 0

                # Calculate study time
                study_time = sum(course.get('study_time_minutes', 0) for course in user_data.values()) / 60

                # Determine progress level
                if total_lessons < 5:
                    level = 'beginner'
                elif total_lessons < 15:
                    level = 'intermediate'
                else:
                    level = 'advanced'

                return {
                    'user_id': user_id,
                    'progress_level': level,
                    'lessons_completed': total_lessons,
                    'courses_completed': total_courses,
                    'certificates_earned': total_courses,
                    'average_quiz_score': avg_score,
                    'study_time_hours': study_time,
                    'completion_rate': min(100, (total_lessons / 20) * 100),
                    'last_activity': self._get_last_activity(user_data)
                }
        except Exception as e:
            print(f"Progress tracker error: {e}")

        # Return default stats for new users
        return {
            'user_id': user_id,
            'progress_level': 'beginner',
            'lessons_completed': 0,
            'courses_completed': 0,
            'certificates_earned': 0,
            'average_quiz_score': 0,
            'study_time_hours': 0,
            'completion_rate': 0,
            'last_activity': 'Never'
        }

    def _get_last_activity(self, user_data):
        """Get user's last activity date"""
        last_dates = []
        for course in user_data.values():
            if 'last_accessed' in course:
                last_dates.append(course['last_accessed'])

        if last_dates:
            return max(last_dates)
        return 'Never'

    def update_progress(self, user_id, course_id, lesson_id, quiz_score=None):
        """Update user's learning progress"""
        try:
            if os.path.exists(self.progress_file):
                with open(self.progress_file, 'r') as f:
                    progress_data = json.load(f)
            else:
                progress_data = {}

            if str(user_id) not in progress_data:
                progress_data[str(user_id)] = {}

            if course_id not in progress_data[str(user_id)]:
                progress_data[str(user_id)][course_id] = {
                    'completed_lessons': [],
                    'quiz_scores': {},
                    'start_date': datetime.utcnow().isoformat(),
                    'study_time_minutes': 0
                }

            course_data = progress_data[str(user_id)][course_id]

            # Update lesson completion
            if lesson_id not in course_data['completed_lessons']:
                course_data['completed_lessons'].append(lesson_id)

            # Update quiz score
            if quiz_score is not None:
                course_data['quiz_scores'][str(lesson_id)] = quiz_score

            # Update last accessed
            course_data['last_accessed'] = datetime.utcnow().isoformat()

            # Save updated progress
            with open(self.progress_file, 'w') as f:
                json.dump(progress_data, f, indent=2)

            return True

        except Exception as e:
            print(f"Error updating progress: {e}")
            return False

progress_tracker = ProgressTracker()