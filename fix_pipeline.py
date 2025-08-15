#!/usr/bin/env python3
"""
GitHub MCP Server CI/CD Pipeline Fix Tool
This script fixes the CI pipeline by ensuring proper flake8 configuration usage.
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command, cwd=None, capture_output=True):
    """Run a command and return the result."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=capture_output,
            text=True
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)


def check_flake8_config():
    """Check if .flake8 configuration file exists and is properly configured."""
    config_path = Path("automation_framework/.flake8")
    
    if not config_path.exists():
        print("❌ .flake8 configuration file not found!")
        return False
    
    print("✅ .flake8 configuration file found")
    
    # Read and validate configuration
    with open(config_path, 'r') as f:
        config_content = f.read()
    
    print("📋 Current .flake8 configuration:")
    print("-" * 50)
    print(config_content)
    print("-" * 50)
    
    return True


def run_flake8_validation():
    """Run flake8 validation using the configuration file."""
    print("🔍 Running flake8 validation...")
    
    os.chdir("automation_framework")
    return_code, stdout, stderr = run_command("flake8 .")
    
    print(f"Return code: {return_code}")
    
    if stdout:
        print("📋 STDOUT:")
        print(stdout)
    
    if stderr:
        print("📋 STDERR:")
        print(stderr)
    
    if return_code == 0:
        print("✅ Flake8 validation passed!")
        return True
    else:
        print("❌ Flake8 validation failed!")
        return False


def check_python_files():
    """Check individual Python files for flake8 compliance."""
    print("🔍 Checking individual Python files...")
    
    python_files = [
        "automation_framework/utils/logger.py",
        "automation_framework/utils/helper_utils.py",
        "automation_framework/utils/config_manager.py",
        "automation_framework/conftest.py",
        "automation_framework/mcp_integration.py",
        "automation_framework/playwright_mcp_runner.py"
    ]
    
    failed_files = []
    
    for file_path in python_files:
        if os.path.exists(file_path):
            print(f"📁 Checking {file_path}...")
            return_code, stdout, stderr = run_command(
                f"flake8 {file_path} --config=automation_framework/.flake8"
            )
            
            if return_code != 0:
                print(f"❌ {file_path} has flake8 issues:")
                print(stdout)
                failed_files.append(file_path)
            else:
                print(f"✅ {file_path} passed flake8 validation")
        else:
            print(f"⚠️  {file_path} not found")
    
    return failed_files


def create_ci_workflow_fix():
    """Create a fixed CI workflow configuration."""
    print("🚀 Creating fixed CI workflow...")
    
    workflow_content = """name: 🚀 CI Pipeline - GitHub MCP Server Fixed

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:

env:
  PYTHON_VERSION: '3.11'

jobs:
  validate:
    name: 🔍 Validation & Linting
    runs-on: ubuntu-latest
    
    steps:
      - name: 📁 Checkout Repository
        uses: actions/checkout@v4
      
      - name: 🐍 Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
          cache: 'pip'
      
      - name: 📦 Install Dependencies
        run: |
          pip install -r automation_framework/requirements.txt
          pip install flake8 black pytest-cov
      
      - name: 🔍 Code Linting with .flake8 Configuration
        run: |
          cd automation_framework
          echo "Using .flake8 configuration file..."
          cat .flake8
          echo "Running flake8 validation..."
          flake8 .
        continue-on-error: false
      
      - name: ✅ Validation Complete
        run: |
          echo "✅ All validations passed!"
          echo "✅ .flake8 configuration is working correctly"
          echo "✅ GitHub MCP Server CI/CD pipeline is fixed"
"""
    
    # Save to local file for reference
    with open("ci-workflow-fixed.yml", "w") as f:
        f.write(workflow_content)
    
    print("✅ Fixed CI workflow saved to ci-workflow-fixed.yml")
    return workflow_content


def main():
    """Main execution function."""
    print("🚀 GitHub MCP Server CI/CD Pipeline Fix Tool")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists("automation_framework"):
        print("❌ automation_framework directory not found!")
        print("Please run this script from the project root directory.")
        sys.exit(1)
    
    success = True
    
    # Step 1: Check .flake8 configuration
    print("📋 Step 1: Checking .flake8 configuration...")
    if not check_flake8_config():
        success = False
    
    # Step 2: Run flake8 validation
    print("\\n📋 Step 2: Running flake8 validation...")
    if not run_flake8_validation():
        success = False
    
    # Step 3: Check individual files
    print("\\n📋 Step 3: Checking individual Python files...")
    failed_files = check_python_files()
    if failed_files:
        print(f"❌ {len(failed_files)} files failed validation: {failed_files}")
        success = False
    
    # Step 4: Create fixed workflow
    print("\\n📋 Step 4: Creating fixed CI workflow...")
    create_ci_workflow_fix()
    
    # Final summary
    print("\\n" + "=" * 60)
    if success:
        print("✅ SUCCESS: All validations passed!")
        print("✅ The .flake8 configuration is working correctly")
        print("✅ CI pipeline should now work with the fixed configuration")
        print("\\n📋 Next Steps:")
        print("1. The ci-workflow-fixed.yml file has been created")
        print("2. Replace the current CI workflow with this fixed version")
        print("3. The pipeline will use the .flake8 configuration file")
        print("4. All Python code should pass linting")
    else:
        print("❌ FAILURE: Some validations failed")
        print("❌ Please fix the issues above before proceeding")
        print("\\n🔧 Recommendations:")
        print("1. Check the .flake8 configuration file")
        print("2. Fix any Python code linting issues")
        print("3. Re-run this validation script")
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())