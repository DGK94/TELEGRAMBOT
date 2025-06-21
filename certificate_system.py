
<line_number>1</line_number>
import json
import os
from datetime import datetime
import hashlib
import uuid

class OfficialCertificateSystem:
    def __init__(self):
        self.certificates_file = "trading_academy/official_certificates.json"
        self.verification_file = "trading_academy/certificate_verification.json"
        self.setup_certificate_templates()
    
    def setup_certificate_templates(self):
        """Initialize official certificate templates"""
        certificate_templates = {
            "institutions": {
                "signalxpress_academy": {
                    "name": "SignalXpress Professional Trading Academy",
                    "accreditation": "International Trading Education Council (ITEC)",
                    "certificate_id_prefix": "SXP-CERT",
                    "verification_url": "https://academy.signalxpress.pro/verify/",
                    "logo_url": "https://academy.signalxpress.pro/assets/official_seal.png"
                },
                "blockchain_institute": {
                    "name": "Blockchain Technology Institute",
                    "accreditation": "Global Blockchain Education Alliance (GBEA)",
                    "certificate_id_prefix": "BTI-CERT",
                    "verification_url": "https://blockchain-institute.org/verify/",
                    "logo_url": "https://blockchain-institute.org/assets/seal.png"
                }
            },
            "course_certifications": {
                "technical_analysis_basics": {
                    "certificate_title": "Professional Technical Analysis Certification",
                    "level": "Foundation",
                    "credits": 40,
                    "requirements": {
                        "min_lessons_completed": 5,
                        "min_quiz_score": 80,
                        "final_exam_score": 85
                    },
                    "skills_certified": [
                        "Chart pattern recognition",
                        "Support/resistance identification", 
                        "Technical indicator analysis",
                        "Risk assessment",
                        "Trade planning"
                    ]
                },
                "bitcoin_mastery": {
                    "certificate_title": "Bitcoin Professional Certification",
                    "level": "Specialist",
                    "credits": 60,
                    "requirements": {
                        "min_lessons_completed": 8,
                        "min_quiz_score": 85,
                        "final_exam_score": 90
                    },
                    "skills_certified": [
                        "Bitcoin network analysis",
                        "Halving cycle trading",
                        "Institutional accumulation patterns",
                        "Lightning Network utilization",
                        "Macro economic correlation"
                    ]
                },
                "chia_farming": {
                    "certificate_title": "Chia Network Farming Professional",
                    "level": "Specialist", 
                    "credits": 45,
                    "requirements": {
                        "min_lessons_completed": 5,
                        "min_quiz_score": 80,
                        "final_exam_score": 85
                    },
                    "skills_certified": [
                        "Proof of Space optimization",
                        "Hardware configuration",
                        "Pool farming strategies",
                        "ROI calculation",
                        "Sustainable blockchain technology"
                    ]
                },
                "risk_management": {
                    "certificate_title": "Professional Risk Management Certification",
                    "level": "Foundation",
                    "credits": 35,
                    "requirements": {
                        "min_lessons_completed": 4,
                        "min_quiz_score": 85,
                        "final_exam_score": 90
                    },
                    "skills_certified": [
                        "Position sizing calculation",
                        "Stop loss placement",
                        "Risk-reward optimization",
                        "Portfolio diversification",
                        "Psychology of risk"
                    ]
                },
                "algorithmic_trading": {
                    "certificate_title": "Algorithmic Trading Professional Certification",
                    "level": "Advanced",
                    "credits": 80,
                    "requirements": {
                        "min_lessons_completed": 10,
                        "min_quiz_score": 85,
                        "final_exam_score": 90
                    },
                    "skills_certified": [
                        "Python trading development",
                        "API integration",
                        "Strategy backtesting",
                        "Risk automation",
                        "High-frequency trading"
                    ]
                }
            }
        }
        
        try:
            with open(self.certificates_file, 'w') as f:
                json.dump(certificate_templates, f, indent=2)
        except Exception as e:
            print(f"Error creating certificate templates: {e}")
    
    def generate_certificate_id(self, user_id, course_id):
        """Generate unique certificate ID with verification hash"""
        timestamp = str(int(datetime.utcnow().timestamp()))
        unique_string = f"{user_id}-{course_id}-{timestamp}-{uuid.uuid4().hex[:8]}"
        cert_hash = hashlib.sha256(unique_string.encode()).hexdigest()[:16]
        return f"SXP-{cert_hash.upper()}"
    
    def issue_official_certificate(self, user_id, course_id, user_progress):
        """Issue official certificate with verification"""
        try:
            # Load certificate templates
            with open(self.certificates_file, 'r') as f:
                templates = json.load(f)
            
            course_template = templates["course_certifications"].get(course_id)
            if not course_template:
                return None
            
            # Check requirements
            completed_lessons = len(user_progress.get("completed_lessons", []))
            quiz_scores = user_progress.get("quiz_scores", {})
            avg_quiz_score = sum(quiz_scores.values()) / len(quiz_scores) if quiz_scores else 0
            
            requirements = course_template["requirements"]
            if (completed_lessons < requirements["min_lessons_completed"] or 
                avg_quiz_score < requirements["min_quiz_score"]):
                return None
            
            # Generate certificate
            certificate_id = self.generate_certificate_id(user_id, course_id)
            issue_date = datetime.utcnow().isoformat()
            
            certificate = {
                "certificate_id": certificate_id,
                "holder_id": user_id,
                "course_id": course_id,
                "certificate_title": course_template["certificate_title"],
                "level": course_template["level"],
                "credits": course_template["credits"],
                "skills_certified": course_template["skills_certified"],
                "institution": templates["institutions"]["signalxpress_academy"],
                "issue_date": issue_date,
                "expiry_date": None,  # Professional certifications don't expire
                "verification_url": f"https://academy.signalxpress.pro/verify/{certificate_id}",
                "performance_metrics": {
                    "lessons_completed": completed_lessons,
                    "average_quiz_score": round(avg_quiz_score, 1),
                    "completion_time_days": self._calculate_completion_time(user_progress)
                },
                "verification_hash": self._generate_verification_hash(certificate_id, user_id, course_id, issue_date)
            }
            
            # Save to verification database
            self._save_certificate_verification(certificate)
            
            return certificate
            
        except Exception as e:
            print(f"Certificate generation error: {e}")
            return None
    
    def _generate_verification_hash(self, cert_id, user_id, course_id, issue_date):
        """Generate verification hash for certificate authenticity"""
        verification_string = f"{cert_id}-{user_id}-{course_id}-{issue_date}-SIGNALXPRESS"
        return hashlib.sha256(verification_string.encode()).hexdigest()
    
    def _save_certificate_verification(self, certificate):
        """Save certificate to verification database"""
        try:
            if os.path.exists(self.verification_file):
                with open(self.verification_file, 'r') as f:
                    verifications = json.load(f)
            else:
                verifications = {}
            
            verifications[certificate["certificate_id"]] = {
                "holder_id": certificate["holder_id"],
                "course_id": certificate["course_id"], 
                "issue_date": certificate["issue_date"],
                "verification_hash": certificate["verification_hash"],
                "status": "valid"
            }
            
            with open(self.verification_file, 'w') as f:
                json.dump(verifications, f, indent=2)
                
        except Exception as e:
            print(f"Verification save error: {e}")
    
    def _calculate_completion_time(self, user_progress):
        """Calculate course completion time in days"""
        try:
            start_date = datetime.fromisoformat(user_progress.get("start_date", datetime.utcnow().isoformat()))
            end_date = datetime.utcnow()
            return (end_date - start_date).days
        except:
            return 0
    
    def verify_certificate(self, certificate_id):
        """Verify certificate authenticity"""
        try:
            with open(self.verification_file, 'r') as f:
                verifications = json.load(f)
            
            return verifications.get(certificate_id, {})
        except:
            return {}
    
    def format_certificate_display(self, certificate):
        """Format certificate for display in Telegram"""
        return f"""🏆 **OFFICIAL CERTIFICATE ISSUED**

📜 **{certificate['certificate_title']}**
🎓 Level: {certificate['level']} | Credits: {certificate['credits']}

👤 **Certificate ID:** `{certificate['certificate_id']}`
📅 **Issue Date:** {certificate['issue_date'][:10]}
🏛️ **Institution:** {certificate['institution']['name']}

✅ **Skills Certified:**
{chr(10).join([f"• {skill}" for skill in certificate['skills_certified']])}

📊 **Performance:**
• Lessons Completed: {certificate['performance_metrics']['lessons_completed']}
• Average Quiz Score: {certificate['performance_metrics']['average_quiz_score']}%
• Completion Time: {certificate['performance_metrics']['completion_time_days']} days

🔗 **Verification:** {certificate['verification_url']}

*This certificate is officially recognized by the International Trading Education Council (ITEC)*"""

# Global certificate system instance
cert_system = OfficialCertificateSystem()
