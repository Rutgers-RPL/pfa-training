# Check if conda is installed
$condaInstalled = Get-Command conda -ErrorAction SilentlyContinue

if ($condaInstalled) {
    # Check if conda initialization was successful
    $condaInitialized = conda info --envs

    if ($condaInitialized) {
        Write-Output "conda test OK"
    } else {
        Write-Output "Conda is installed but initialization failed."
    }
} else {
    Write-Output "Conda is not installed."
}
