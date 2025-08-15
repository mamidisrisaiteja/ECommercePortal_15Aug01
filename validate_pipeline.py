#!/usr/bin/env python3
"""
GitHub MCP Server CI/CD Pipeline Test Script
This script validates that our flake8 configuration works correctly.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_flake8_validation():
    """Run flake8 validation using our configuration."""
    print("🔍 Running flake8 validation with GitHub MCP Server configuration...")
    
    # Change to automation_framework directory
    automation_dir = Path(__file__).parent / "automation_framework"
    if not automation_dir.exists():
        print("❌ automation_framework directory not found!")
        return False
    
    try:
        # Run flake8 with our configuration
        result = subprocess.run(
            ["flake8", ".", "--config=.flake8"],
            cwd=automation_dir,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ Flake8 validation passed!")
            print("✅ All Python files comply with our coding standards")
            return True
        else:
            print("❌ Flake8 validation failed:")
            print(result.stdout)
            print(result.stderr)
            return False
            
    except FileNotFoundError:
        print("❌ flake8 not found. Please install it with: pip install flake8")
        return False


def check_github_mcp_integration():
    """Check if GitHub MCP integration files are present."""
    print("\n🤖 Checking GitHub MCP Server integration...")
    
    required_files = [
        "automation_framework/mcp_integration.py",
        "automation_framework/playwright_mcp_runner.py",
        ".github/workflows/ci.yml",
        ".github/workflows/regression-tests.yml",
        ".github/workflows/mcp-integration.yml"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"⚠️  Missing GitHub MCP files: {missing_files}")
        return False
    else:
        print("✅ All GitHub MCP Server integration files are present")
        return True


def main():
    """Main execution function."""
    print("🚀 GitHub MCP Server CI/CD Pipeline Validation")
    print("=" * 50)
    
    # Check current working directory
    print(f"📁 Current directory: {os.getcwd()}")
    
    # Run validations
    flake8_passed = run_flake8_validation()
    mcp_files_present = check_github_mcp_integration()
    
    print("\n📊 Validation Summary:")
    print(f"{'✅' if flake8_passed else '❌'} Flake8 Code Quality: {'PASSED' if flake8_passed else 'FAILED'}")
    print(f"{'✅' if mcp_files_present else '❌'} MCP Integration Files: {'PRESENT' if mcp_files_present else 'MISSING'}")
    
    if flake8_passed and mcp_files_present:
        print("\n🎉 All validations passed! Ready for GitHub MCP Server CI/CD pipeline!")
        return 0
    else:
        print("\n⚠️  Some validations failed. Please check the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())