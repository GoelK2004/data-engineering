$watchFolder = "C:\...\Week5\Task2\EventTrigger\fileArrival"
$filter = "*.csv"
$sqlServer = "localhost"
$database = "bikeStoresRep"
$jobName = "fileArrival"

# Load SQL Server module
Import-Module SqlServer -ErrorAction SilentlyContinue

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $watchFolder
$watcher.Filter = $filter
$watcher.EnableRaisingEvents = $true
$watcher.IncludeSubdirectories = $false

Register-ObjectEvent $watcher "Created" -Action {
    $fileName = $Event.SourceEventArgs.Name
    $fullPath = Join-Path $watchFolder $fileName
    Write-Host "File detected: $fullPath"

    try {
        # Insert file path into SQL Server queue
        $insertQuery = @"
INSERT INTO fl.FileQueue (file_path)
VALUES (N'$fullPath');
"@
        Invoke-Sqlcmd -ServerInstance $sqlServer -Database $database -Query $insertQuery

        # Start the SQL Server Agent job
        Invoke-Sqlcmd -ServerInstance $sqlServer -Database "msdb" -Query "
            EXEC msdb.dbo.sp_start_job @job_name = N'$jobName';
        "

        Write-Host "Job triggered for file: $fileName"
    }
    catch {
        Write-Host "ERROR: $_"
    }
}


Write-Host "Watching $watchFolder for new files. Press Ctrl+C to stop."

while ($true) { Start-Sleep -Seconds 5 }
