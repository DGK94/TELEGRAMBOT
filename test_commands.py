
#!/usr/bin/env python3
"""
Comprehensive command testing script for SignalXpress Pro Bot
Tests all commands for functionality and proper responses
"""

import asyncio
import logging
from unittest.mock import Mock, MagicMock
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the main bot functions
from main import *

class BotTester:
    def __init__(self):
        self.test_results = {}
        self.total_tests = 0
        self.passed_tests = 0
        
    async def mock_update_context(self, command_text="/start", user_id=12345):
        """Create mock update and context objects"""
        update = Mock()
        context = Mock()
        
        # Mock update object
        update.effective_user = Mock()
        update.effective_user.id = user_id
        update.effective_user.username = "testuser"
        update.effective_user.is_bot = False
        
        update.message = Mock()
        update.message.text = command_text
        update.message.reply_text = MagicMock()
        update.message.reply_photo = MagicMock()
        
        # Mock context object
        context.args = command_text.split()[1:] if len(command_text.split()) > 1 else []
        context.bot = Mock()
        context.bot.send_message = MagicMock()
        
        return update, context
    
    async def test_command(self, command_name, command_func, test_args=None):
        """Test a single command function"""
        self.total_tests += 1
        
        try:
            command_text = f"/{command_name}"
            if test_args:
                command_text += f" {' '.join(test_args)}"
                
            update, context = await self.mock_update_context(command_text)
            
            # Override args if provided
            if test_args:
                context.args = test_args
            
            # Execute the command
            await command_func(update, context)
            
            # Check if reply was called
            response_sent = (update.message.reply_text.called or 
                           update.message.reply_photo.called or
                           context.bot.send_message.called)
            
            if response_sent:
                self.test_results[command_name] = "✅ PASS"
                self.passed_tests += 1
                print(f"✅ {command_name}: PASSED")
            else:
                self.test_results[command_name] = "❌ FAIL - No response"
                print(f"❌ {command_name}: FAILED - No response sent")
                
        except Exception as e:
            self.test_results[command_name] = f"❌ ERROR - {str(e)[:50]}"
            print(f"❌ {command_name}: ERROR - {e}")
            
    async def run_all_tests(self):
        """Run comprehensive tests for all bot commands"""
        print("🚀 Starting SignalXpress Pro Bot Command Tests\n")
        
        # Test all main commands
        test_commands = [
            ("start", start),
            ("signal", signal),
            ("multisignal", multi_asset_signals),
            ("market", market_overview),
            ("portfolio", portfolio_command),
            ("ai", ai_market_predictions),
            ("predict", ai_price_prediction, ["BTC", "24h"]),
            ("compare", crypto_comparison, ["BTC", "ETH"]),
            ("whale", whale_tracker),
            ("blockchain", blockchain_analysis),
            ("alerts", trade_alerts_command),
            ("education", trading_education),
            ("news", crypto_news_feed),
            ("defi", defi_staking_info),
            ("heatmap", crypto_heatmap),
            ("social", social_sentiment),
            ("fear", fear_greed_index),
            ("calendar", economic_calendar),
            ("screener", market_screener),
            ("liquidations", liquidation_tracker),
            ("funding", funding_rates),
            ("arbitrage", arbitrage_opportunities),
            ("options", options_flow),
            ("realtime", realtime_analysis),
            ("progress", user_progress),
            ("quiz", quiz_command, ["crypto_basics"]),
            ("status", system_status),
            ("help", command_help)
        ]
        
        # Run tests
        for test_data in test_commands:
            command_name = test_data[0]
            command_func = test_data[1]
            test_args = test_data[2] if len(test_data) > 2 else None
            
            await self.test_command(command_name, command_func, test_args)
            await asyncio.sleep(0.1)  # Small delay between tests
            
        # Print summary
        print(f"\n📊 TEST SUMMARY:")
        print(f"Total Commands Tested: {self.total_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.total_tests - self.passed_tests}")
        print(f"Success Rate: {(self.passed_tests/self.total_tests)*100:.1f}%")
        
        print(f"\n📋 DETAILED RESULTS:")
        for command, result in self.test_results.items():
            print(f"/{command}: {result}")
            
        # Return overall success
        return self.passed_tests == self.total_tests

async def main():
    """Main test runner"""
    # Setup logging to suppress unnecessary output during testing
    logging.basicConfig(level=logging.ERROR)
    
    tester = BotTester()
    success = await tester.run_all_tests()
    
    if success:
        print("\n🎉 ALL TESTS PASSED! Bot is fully functional.")
        return 0
    else:
        print("\n⚠️ Some tests failed. Check the results above.")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
