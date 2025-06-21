
import asyncio
import logging
import time
import psutil
import os
from datetime import datetime
import requests

class HealthMonitor:
    def __init__(self):
        self.start_time = time.time()
        self.health_status = "HEALTHY"
        self.last_check = datetime.utcnow()
        
    async def check_system_health(self):
        """Comprehensive system health check"""
        health_report = {
            'timestamp': datetime.utcnow().isoformat(),
            'uptime_seconds': time.time() - self.start_time,
            'status': 'HEALTHY'
        }
        
        try:
            # CPU and memory check
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            health_report.update({
                'cpu_percent': cpu_percent,
                'memory_percent': memory.percent,
                'disk_percent': disk.percent,
                'memory_available_gb': memory.available / (1024**3),
                'disk_free_gb': disk.free / (1024**3)
            })
            
            # Check critical thresholds
            if cpu_percent > 90:
                health_report['status'] = 'WARNING'
                health_report['issues'] = health_report.get('issues', [])
                health_report['issues'].append('High CPU usage')
                
            if memory.percent > 85:
                health_report['status'] = 'WARNING'
                health_report['issues'] = health_report.get('issues', [])
                health_report['issues'].append('High memory usage')
                
            if disk.percent > 90:
                health_report['status'] = 'CRITICAL'
                health_report['issues'] = health_report.get('issues', [])
                health_report['issues'].append('Low disk space')
            
            # Test API connectivity
            try:
                response = requests.get('https://api.binance.com/api/v3/ping', timeout=5)
                health_report['api_connectivity'] = 'OK' if response.status_code == 200 else 'FAILED'
            except:
                health_report['api_connectivity'] = 'FAILED'
                health_report['status'] = 'WARNING'
                health_report['issues'] = health_report.get('issues', [])
                health_report['issues'].append('API connectivity issues')
            
            # Check file system permissions
            try:
                test_file = 'health_test.tmp'
                with open(test_file, 'w') as f:
                    f.write('test')
                os.remove(test_file)
                health_report['file_system'] = 'OK'
            except:
                health_report['file_system'] = 'FAILED'
                health_report['status'] = 'CRITICAL'
                health_report['issues'] = health_report.get('issues', [])
                health_report['issues'].append('File system access failed')
            
            self.last_check = datetime.utcnow()
            return health_report
            
        except Exception as e:
            logging.error(f"Health check failed: {e}")
            return {
                'timestamp': datetime.utcnow().isoformat(),
                'status': 'CRITICAL',
                'error': str(e)
            }
    
    def get_uptime_formatted(self):
        """Get formatted uptime string"""
        uptime_seconds = time.time() - self.start_time
        hours = int(uptime_seconds // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        return f"{hours}h {minutes}m"

# Global health monitor
health_monitor = HealthMonitor()

async def main():
    """Test health monitoring"""
    monitor = HealthMonitor()
    health = await monitor.check_system_health()
    print(f"Health Status: {health['status']}")
    print(f"Uptime: {monitor.get_uptime_formatted()}")
    print(f"CPU: {health.get('cpu_percent', 0):.1f}%")
    print(f"Memory: {health.get('memory_percent', 0):.1f}%")
    print(f"API: {health.get('api_connectivity', 'Unknown')}")

if __name__ == "__main__":
    asyncio.run(main())
