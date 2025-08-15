# GitHub Repository Creation Script for ECommercePortal_15Aug01
# This script creates a new GitHub repository using GitHub API

Write-Host "🚀 Creating GitHub Repository: ECommercePortal_15Aug01" -ForegroundColor Green

# Repository configuration
$repoName = "ECommercePortal_15Aug01"
$description = "Test Automation Framework for E-Commerce Portal using Playwright MCP Server, Python, Pytest, and BDD"
$private = $false  # Set to $true if you want a private repository

# Check if GitHub CLI is installed
try {
    $ghVersion = gh --version
    Write-Host "✅ GitHub CLI found: $($ghVersion[0])" -ForegroundColor Green
} catch {
    Write-Host "❌ GitHub CLI not found. Please install GitHub CLI first:" -ForegroundColor Red
    Write-Host "   Visit: https://cli.github.com/" -ForegroundColor Yellow
    Write-Host "   Or run: winget install --id GitHub.cli" -ForegroundColor Yellow
    exit 1
}

# Check if user is authenticated
try {
    $authStatus = gh auth status 2>&1
    if ($authStatus -match "Logged in to github.com") {
        Write-Host "✅ Already authenticated with GitHub" -ForegroundColor Green
    } else {
        Write-Host "🔐 Authenticating with GitHub..." -ForegroundColor Yellow
        gh auth login
    }
} catch {
    Write-Host "🔐 Please authenticate with GitHub first..." -ForegroundColor Yellow
    gh auth login
}

# Create the repository
Write-Host "📁 Creating repository: $repoName" -ForegroundColor Cyan

try {
    if ($private) {
        gh repo create $repoName --description $description --private
    } else {
        gh repo create $repoName --description $description --public
    }
    
    Write-Host "✅ Repository created successfully!" -ForegroundColor Green
    Write-Host "🌐 Repository URL: https://github.com/$(gh api user --jq .login)/$repoName" -ForegroundColor Cyan
    
    # Clone the repository locally
    $cloneChoice = Read-Host "Would you like to clone the repository locally? (y/n)"
    if ($cloneChoice -eq "y" -or $cloneChoice -eq "Y") {
        Write-Host "📥 Cloning repository..." -ForegroundColor Cyan
        gh repo clone $repoName
        Write-Host "✅ Repository cloned to: .\$repoName" -ForegroundColor Green
        
        # Ask if user wants to initialize with framework files
        $initChoice = Read-Host "Would you like to copy the automation framework files to the repository? (y/n)"
        if ($initChoice -eq "y" -or $initChoice -eq "Y") {
            Write-Host "📋 Copying automation framework files..." -ForegroundColor Cyan
            
            # Copy automation framework to the cloned repository
            $sourcePath = "automation_framework"
            $destPath = ".\$repoName\automation_framework"
            
            if (Test-Path $sourcePath) {
                Copy-Item -Path $sourcePath -Destination $destPath -Recurse -Force
                Write-Host "✅ Framework files copied successfully!" -ForegroundColor Green
                
                # Navigate to repository and add files
                Set-Location $repoName
                git add .
                git commit -m "Initial commit: Add Playwright MCP Test Automation Framework

- Complete BDD framework with Cucumber features
- Page Object Model implementation  
- Playwright MCP server integration
- Generated test cases for E-commerce scenarios
- Configuration files and documentation
- Test scenarios: Authentication, Inventory, Cart modules"
                
                git push origin main
                Write-Host "✅ Files pushed to GitHub successfully!" -ForegroundColor Green
                Write-Host "🎉 Your automation framework is now on GitHub!" -ForegroundColor Magenta
            } else {
                Write-Host "⚠️  Automation framework folder not found at: $sourcePath" -ForegroundColor Yellow
                Write-Host "   Please make sure you're running this script from the correct directory" -ForegroundColor Yellow
            }
        }
    }
    
} catch {
    Write-Host "❌ Error creating repository: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

Write-Host "`n🎉 GitHub repository setup completed!" -ForegroundColor Magenta
Write-Host "📚 Next steps:" -ForegroundColor Yellow
Write-Host "   1. Visit your repository on GitHub" -ForegroundColor White
Write-Host "   2. Add collaborators if needed" -ForegroundColor White
Write-Host "   3. Set up branch protection rules" -ForegroundColor White
Write-Host "   4. Configure GitHub Actions for CI/CD" -ForegroundColor White
